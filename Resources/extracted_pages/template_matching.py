import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from sklearn.cluster import DBSCAN
from collections import defaultdict
import argparse

def match_templates(image_path, templates, template_strings, scales, threshold, eps):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_color = cv2.imread(image_path)  # fresh copy for final drawing
    all_results = []

    for template_path, template_string in zip(templates, template_strings):
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

        for scale in scales:
            scaled_template = cv2.resize(template, None, fx=scale, fy=scale)
            h, w = scaled_template.shape[:2]

            match = cv2.matchTemplate(image, scaled_template, cv2.TM_CCOEFF_NORMED)
            locations = np.where(match >= threshold)

            for pt in zip(*locations[::-1]):
                x, y = pt
                if (x + w <= image.shape[1]) and (y + h <= image.shape[0]):
                    matched_region = image[y:y + h, x:x + w]
                    matched_region_resized = cv2.resize(matched_region, (w, h))
                    score = ssim(scaled_template, matched_region_resized)

                    all_results.append(
                        {
                            "template_string": template_string,
                            "confidence": score,
                            "position": ((x, y), (x + w, y + h)),
                            "scale": scale,
                        }
                    )

    cleaned_results = deduplicate_and_keep_best(all_results)
    assert len(cleaned_results) > 0, "No results found, consider different scales"
    cleaned_results = cluster_and_sort(cleaned_results, eps=eps)

    for res in cleaned_results:
        (x1, y1), (x2, y2) = res["position"]
        template_str = res["template_string"]
        cv2.rectangle(image_color, (x1, y1), (x2, y2), (0, 255, 0), 1)
        cv2.putText(
            image_color,
            template_str,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )

    return cleaned_results, image_color

def cluster_and_sort(cleaned_results, eps):
    y_centers = [[(r["position"][0][1] + r["position"][1][1]) / 2] for r in cleaned_results]
    db = DBSCAN(eps=eps, min_samples=1).fit(np.array(y_centers))
    clusters = defaultdict(list)

    for i, lbl in enumerate(db.labels_):
        clusters[lbl].append(cleaned_results[i])

    for lbl in clusters:
        clusters[lbl].sort(key=lambda r: r["position"][0][0])

    sorted_labels = sorted(
        clusters.keys(),
        key=lambda lbl: np.mean(
            [(r["position"][0][1] + r["position"][1][1]) / 2 for r in clusters[lbl]]
        ),
    )

    final_sorted = [r for lbl in sorted_labels for r in clusters[lbl]]
    return final_sorted

def deduplicate_and_keep_best(results, overlap_threshold=0.5):
    results_sorted = sorted(results, key=lambda r: r["confidence"], reverse=True)
    final = []

    for candidate in results_sorted:
        (cx1, cy1), (cx2, cy2) = candidate["position"]
        keep = True
        for accepted in final:
            (ax1, ay1), (ax2, ay2) = accepted["position"]
            if boxes_overlap((cx1, cy1, cx2, cy2), (ax1, ay1, ax2, ay2), overlap_threshold):
                keep = False
                break
        if keep:
            final.append(candidate)

    return final

def boxes_overlap(boxA, boxB, thresh):
    (Ax1, Ay1, Ax2, Ay2) = boxA
    (Bx1, By1, Bx2, By2) = boxB

    interX1, interY1 = max(Ax1, Bx1), max(Ay1, By1)
    interX2, interY2 = min(Ax2, Bx2), min(Ay2, By2)
    interW, interH = max(0, interX2 - interX1), max(0, interY2 - interY1)
    intersection = interW * interH

    areaA, areaB = (Ax2 - Ax1) * (Ay2 - Ay1), (Bx2 - Bx1) * (By2 - By1)
    if areaA == 0 or areaB == 0:
        return False

    return intersection / float(min(areaA, areaB)) > thresh

def extract_sequences(results):
    return "".join([r["template_string"] for r in results])

def extract_sub_sequence(sequence, start_substring, end_substring):
    start_index, end_index = sequence.find(start_substring), sequence.find(end_substring)
    if start_index != -1 and end_index != -1 and end_index > start_index:
        return sequence[start_index:end_index + len(end_substring)]
    return "Start or end substring not found, or end occurs before start."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Template Matching Script")
    parser.add_argument("--image_path", type=str, required=True, help="Path to input image")
    parser.add_argument("--templates", nargs="+", required=True, help="List of template image paths")
    parser.add_argument("--template_strings", nargs="+", required=True, help="List of template strings")
    parser.add_argument("--scales", nargs="+", type=float, required=True, help="List of scales to use")
    parser.add_argument("--threshold", type=float, required=True, help="Matching threshold")
    parser.add_argument("--eps", type=float, required=True, help="Epsilon value for clustering")
    parser.add_argument("--output_image", type=str, required=True, help="Path to save output image")
    parser.add_argument("--output_text", type=str, required=True, help="Path to save output text")
    parser.add_argument("--start_strings", type=str, required=True, help="Starting substring for extraction")
    parser.add_argument("--end_strings", type=str, required=True, help="Ending substring for extraction")

    args = parser.parse_args()

    scales = np.linspace(args.scales[0], args.scales[1], int(args.scales[2]))

    results, image_color = match_templates(
        args.image_path, args.templates, args.template_strings, scales, args.threshold, args.eps
    )

    cv2.imwrite(args.output_image, image_color)

    sequences = extract_sequences(results)
    subsequence = extract_sub_sequence(sequences, args.start_strings, args.end_strings)
    with open(str(args.output_text + "full_text"), "w") as f:
        f.write(subsequence)

    with open(args.output_text, "w") as f:
        f.write(subsequence)
