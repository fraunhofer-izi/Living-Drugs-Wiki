---
hide:
  - navigation
  - toc
---
# Sequence Retrieval and Annotation Process
## Sequences (fasta)
All DNA sequences were extracted from various sources (see table below) using a Jupyter Notebook script (`translate_sequences.ipynb`). This process leverages a custom template matching approach implemented in the Python script `template_matching.py`. The method applies structural similarity (SSIM) to detect nucleotide templates (A, C, G, T) from .png images and accurately reconstruct them into a nucleotide sequence string. Annotation process is desribed below. 

**Code**: [translate_sequences.ipynb](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/translate_sequences.ipynb?ref_type=heads)

---

### 📌 Sources of Sequences

| **CAR Construct** | **Source** | **CAR Sequence** | **Vector Sequence** |
|------------------|-----------|------------------|----------------|
| **Ciltacel** | Patent *WO2022116086A1* | SeqID No. 9–17 | NA |
| **Oezdemirli (Ciltacel)** | Supplementary Figure S1 from: [Ozdemirli M et al](https://doi.org/10.1056/NEJMoa2401530) | Nucleotide sequence of the CAR construct (highlighted in light blue) |  From 5'UTR to 3'UTR |
| **Idecel** | Patent *WO2021091978A1* | Sequence No. 10 | Sequence No. 36 |
| **Tisacel** | Patent *US 9,499,629 B2* | SeqID No. 8 | SeqID No. 1 |
| **Axicel** | DrugBank via "Axicel" search referenced: [Roberts ZJ et al.](https://doi.org/10.1080/10428194.2017.1387905) :arrow_right: Roberts et al. referenced: [Kochenderfer JN et al.](https://doi.org/10.1097/CJI.0b013e3181ac6138) :arrow_right: Kochenderfer JN et al. referenced *HM852952*  | Genbank Identifier *HM852952*  | NA |

## Annotations (gtf)
### 1. Download known protein sequences
For annotation, known nucleotide sequences of CAR construct parts were retrieved from NCBI, following the schematic from: [Grahnert et al., Biomedicines (2020)](https://doi.org/10.3390/biomedicines12081641)

**Domains retrieved**:  
- CD28, CD3ζ, 41BB, CD8, CSF2RA  
- Accession numbers: `"NM_001378516.1", "NM_171827.4", "NM_001561.6", "NM_001410981.1", "NR_027760.3"`

**Fetched Sequences**:  
[`fetched_sequences.fasta`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/fetched_sequences.fasta?ref_type=heads)

### 2. Comparison with known annotations
Each CAR construct was aligned against the retrieved domain sequences using BLAST. When applicable, annotations were compared with the original source data (`annotation_from_nucleotide_seq.json`) and compiled into a `.gtf` file.

- **Full Annotation Script**: [`get_annotations.py`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/1b1148904205e7c43620f96ab9d8ebc27f621b18/Resources/extracted_pages/get_annotations.py)
- **Annotation File**: [`annotation_from_nucleotide_seq.json`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/annotation_from_nucleotide_seq.json?ref_type=heads)

### 3. Comparison with DNA domain prediction
All CAR sequences were additionally translated into protein sequence, and screened for protein domains with [SMART](http://smart.embl-heidelberg.de/smart). Based on protein position of predicted domains, nucleotide sequences were extracted [`find_nucleotide_from_protein.py`](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/find_nucleotide_from_protein.py?ref_type=heads).
