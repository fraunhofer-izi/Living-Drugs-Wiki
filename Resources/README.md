# Resource for CAR T profiling

This repository further includes a collection of FDA-approved CAR constructs (annotations and vector sequences for integration site analysis), which serves as a comprehensive resource for researchers and bioinformaticians working with CAR T cell profiling. For further information see [Resources](https://car-flow-david-schmidt-568bf5d68446288a5236b50347863062167cf6c5.ribogitpages.izi.fraunhofer.de/Home/Resources/)

# Explanation of how the sequences have been retrieved and annotated

## Sequences (FASTAS)

### General Information

All DNA sequences were extracted using a Jupyter Notebook script (`translate_sequences.ipynb`) based on a  custom template matching approach (Python script: `template_matching.py`). The method utilizes **structural similarity (SSIM)** to identify nucleotide templates (A, C, G, T) and spatially sort the detected sequence into a string.

**Code**: [translate_sequences.ipynb](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/translate_sequences.ipynb?ref_type=heads)

#### Python Packages Used
- **Image processing & data handling**:  
  `cv2`, `numpy`, `skimage`, `sklearn`, `PIL.Image`, `fitz`
- **Utilities**:  
  `argparse`, `collections`, `shutil`, `re`, `glob`, `subprocess`, `os`

---

## Sequence Details

### **Ciltacel**
- **Source**: Patent *WO2022116086A1*  
- **Extracted Sequences**:
  - **CAR Construct**: SeqID No. 9–17  
  - **Vector Sequence**: No vector sequence included  

---

### **Oezdemirli (Ciltacel)**

- **Publication**: Supplementary Appendix from the article:  
  Ozdemirli M et al., *Indolent CD4+ CAR T-cell lymphoma after cilta-cel CAR T-cell therapy*.  
  *NEJM* 2024; 390:2074-82. DOI: [10.1056/NEJMoa2401530](https://doi.org/10.1056/NEJMoa2401530)
- **Extracted Sequences**:
  - **CAR Construct**: Nucleotide sequence of the CAR construct (highlighted in light blue)  
  - **Vector Sequence**: From **5'UTR** to **3'UTR** of the sequence shown in **Figure S1**  

---

### **Idecel**
- **Source**: Patent *WO2021091978A1*  
- **Extracted Sequences**:
  - **CAR Construct**: Sequence No. 10  
  - **Vector Sequence**: Sequence No. 36  

---

### **Tisacel**
- **Source**: Patent *US 9,499,629 B2*  
- **Extracted Sequences**:
  - **CAR Construct**: SeqID No. 8  
  - **Vector Sequence**: SeqID No. 1  

---

### **Axicel**
- **Source**: Genbank Identifier *HM852952*  
- **Process**:  
  1. DrugBank search referenced:  
     Roberts ZJ et al., *Axicabtagene ciloleucel, a first-in-class CAR T cell therapy for aggressive NHL*.  
     *Leuk Lymphoma*. 2018 Aug;59(8):1785-1796. DOI: [10.1080/10428194.2017.1387905](https://doi.org/10.1080/10428194.2017.1387905)  
  2. Roberts et al. referenced:  
     Kochenderfer JN et al., *Construction and preclinical evaluation of an anti-CD19 chimeric antigen receptor*.  
     *Journal of Immunotherapy*. 2009;32(7):689-702. DOI: [10.1097/CJI.0b013e3181ac6138](https://doi.org/10.1097/CJI.0b013e3181ac6138)  

---


# Annotations

## Download known nucleotide sequences

For all CAR construct annotations, nucleotide sequences of known CAR construct parts were obtained from **NCBI**, following the schematic from:  
Grahnert et al., *Biomedicines* (2020). DOI: [10.3390/biomedicines12081641](https://doi.org/10.3390/biomedicines12081641)

This resulted in a domain list including:
- **Domains**: CD28, CD3zeta, 41bb, CD8, CSF2RA  
- "NM_001378516.1", "NM_171827.4", "NM_001561.6", "NM_001410981.1", "NR_027760.3"]
[`fetched_sequences.fasta`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/fetched_sequences.fasta?ref_type=heads)

### BLAST Analysis and comparison with known annotations
Each CAR construct was aligned against the domain list. Those annotations were compared with the original annotation (when available) [`annotation_from_nucleotide_seq.json`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/annotation_from_nucleotide_seq.json?ref_type=heads) and included in a gtf file.

The complete script can be found at [`get_annotations.py`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/1b1148904205e7c43620f96ab9d8ebc27f621b18/Resources/extracted_pages/get_annotations.py)

## Comparison with DNA domain prediction

All CAR sequences were additionally translated into protein sequence, and screened for protein domains with [SMART](http://smart.embl-heidelberg.de/smart). Based on protein position of predicted domains, nucleotide sequences were extracted [`find_nucleotide_from_protein.py`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/find_nucleotide_from_protein.py?ref_type=heads).