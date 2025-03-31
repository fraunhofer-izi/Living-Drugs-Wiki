# Resource for CAR T profiling

This repository serves as a **resource** to support the analysis and development of CAR T cell therapies by providing comprehensive sequence and annotation data. For original sources and annotation process see [Methods and Scripts](TODO:https://david.schmidt.ribogitpages.izi.fraunhofer.de/living-drugs-wiki/Home/Resources/Methods/).

**CAR constructs** — engineered gene sequences encoding the chimeric antigen receptor — can vary significantly between therapies. These differences require tailored approaches for accurate detection of CAR-positive cells, for example, through single-cell sequencing. :arrow_right: **For a more in-depth explanation about the different CAR constructs see:** [CAR constructs](TODO:./CAR-constructs.md)

In addition, **vector systems** — delivery tools such as viral vectors used to introduce CAR constructs into T cells — play a critical role in determining the efficiency, safety, and stability of gene transfer. Used vector systems themselves differ in key features, such as the type of promoter used, regulatory elements, and backbone sequences, all of which can impact CAR expression and genomic integration. :arrow_right: **For a more in-depth explanation about the vector systems, see:**[Vector systems](TODO:./Vector-systems.md)

For further information see [Resources](TODO:https://car-flow-david-schmidt-568bf5d68446288a5236b50347863062167cf6c5.ribogitpages.izi.fraunhofer.de/Home/Resources/)

# Sequence Retrieval and Annotation Process
## Sequences (fasta)
Sequence information of CAR T cell products (CAR constructs and vectors systems) has been collected from literature and patents (see sources in table below). All DNA sequences were extracted from those sources using a Jupyter Notebook script (`translate_sequences.ipynb`). This process leverages a custom template matching approach implemented in the Python script `template_matching.py`. The method applies structural similarity (SSIM) to detect nucleotide templates (A, C, G, T) from .png images and accurately reconstruct them into a nucleotide sequence string. Annotation process is desribed below. To ensure correct sequences, CAR constructs were manually re-check subsequently.

**Code**: [translate_sequences.ipynb](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/translate_sequences.ipynb?ref_type=heads)

---

### 📌 Sources of Sequences

| **CAR T Cell Product** | **Original Source** | **CAR Sequence** | **Vector Sequence** |
|------------------|-----------|------------------|----------------|
| **Ciltacabtagen autoleucel (Ciltacel)** | Patent *WO2022116086A1* | SeqID No. 9–16 from source | _not available_ |
| **Ciltacabtagen autoleucel (Ciltacel)** | Patent *US20230270786A1* | SeqID No. 9–16 from source | _not available_ |
| **Oezdemirli (Ciltacel)** | Supplementary Figure S1 from: [Ozdemirli M et al](https://doi.org/10.1056/NEJMoa2401530) | Nucleotide sequence of the CAR construct (highlighted in light blue) | Nucleotide sequence from 5'UTR to 3'UTR part|
| **Idecabtagene vicleucel (Idecel)** | Patent *WO2021091978A1* | Sequence No. 10 from source | Sequence No. 36 from source |
| **Tisagenlecleucel (Tisacel)** | Patent *US 9,499,629 B2* | SeqID No. 8 from source | SeqID No. 1 from source |
| **Axicabtagene ciloleucel (Axicel)** | DrugBank search via "Axicel" referenced: [Roberts ZJ et al.](https://doi.org/10.1080/10428194.2017.1387905) :arrow_right: Roberts et al. referenced: [Kochenderfer JN et al.](https://doi.org/10.1097/CJI.0b013e3181ac6138) :arrow_right: Kochenderfer JN et al. referenced *HM852952*  | Genbank Identifier *HM852952*  | NA |

## Annotations (gtf)
### 1. Download known protein sequences
For annotation, known nucleotide sequences of CAR construct parts were retrieved from NCBI, following the schematic from: [Grahnert et al., Biomedicines (2020)](https://doi.org/10.3390/biomedicines12081641)

**Domains retrieved**:  
- CD28, CD3ζ, 41BB, CD8, CSF2RA  
- Accession numbers: `"NM_001378516.1", "NM_171827.4", "NM_001561.6", "NM_001410981.1", "NR_027760.3"`

**Fetched Sequences**:  
[`fetched_sequences.fasta`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/fetched_sequences.fasta?ref_type=heads)

### 2. Comparison with known annotations
Each CAR construct was aligned against the retrieved domain sequences using BLAST. When applicable, annotations were compared with the original source data (`annotation_from_nucleotide_seq.json`) and compiled into a `.gtf` file.

- **Full Annotation Script**: [`get_annotations.py`](https://github.com/fraunhofer-izi/TODO/-/blob/1b1148904205e7c43620f96ab9d8ebc27f621b18/Resources/extracted_pages/get_annotations.py)
- **Annotation File**: [`annotation_from_nucleotide_seq.json`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/annotation_from_nucleotide_seq.json?ref_type=heads)

### 3. Comparison with DNA domain prediction
All CAR sequences were additionally translated into protein sequence, and screened for protein domains with [SMART](http://smart.embl-heidelberg.de/smart). Based on protein position of predicted domains, nucleotide sequences were extracted [`find_nucleotide_from_protein.py`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/find_nucleotide_from_protein.py?ref_type=heads).
