---
hide:
  - navigation
  - toc
---

# Sequence Retrieval and Annotation Process

## Sequences (fasta)

Sequence information on **DNA and protein sequences** of CAR T cell products (CAR constructs and vectors systems) has been collected from literature and patents (see [Sources of Sequences](#sources-of-sequences)). All DNA sequences were extracted from those sources using a Jupyter Notebook script (`translate_sequences.ipynb`). This process leverages a custom template matching approach implemented in the Python script `template_matching.py`. The method applies structural similarity (SSIM) to detect nucleotide templates (A, C, G, T) from .png images and accurately reconstruct them into a nucleotide sequence string. 

All DNA sequences were translated into protein sequences using the [Expasy Translate Tool](https://web.expasy.org/translate/) and saved as `*_protein_translated.fasta` files. For some CAR products, protein sequences were directly provided in the corresponding patents—these original sequences were included whenever available.

!!! note "Discrepancies Between Nucleotide and Protein Sequences"
    In several cases, we observed discrepancies between the nucleotide sequences and the corresponding protein sequences provided in the patents.  
    When translated with [Expasy](https://web.expasy.org/translate/), the nucleotide sequences did not always align with the listed protein sequences.

    For example, in **WO2022116086A1**, the original protein sequence contains an extra `'TS'` that is not supported by the nucleotide sequence—suggesting inconsistencies in the source data.

    **Therefore, both translated and original protein sequences are provided** to ensure transparency and traceability.


The annotation process of CAR constructs and vector systems is desribed below in the [Annotations section](#annotations-gtf).To ensure correct sequences, CAR constructs were manually re-check subsequently.

---

### Sources of Sequences

| **CAR T Cell Product** | **Original Source** | **CAR Sequence (DNA)** | **CAR Sequence (Protein)** | **Vector Sequence** |
|------------------------|----------------------|--------------------------|-----------------------------|----------------------|
| **Ciltacel** | Patent *WO2022116086A1* | SEQ ID NO. 9–16 | SEQ ID NO:17; translated from DNA | _Not available_ |
| **Ciltacel** | Patent *US20230270786A1* | SEQ ID NO. 9–16 | Seq ID NO 17; translated from DNA | _Not available_ |
| **Ciltacel (Oezdemirli et al.)** | Supplementary Figure S1, [Ozdemirli et al.](https://doi.org/10.1056/NEJMoa2401530) | Highlighted DNA sequence of CAR construct | Translated from DNA | Vector sequence from 5'UTR to 3'UTR |
| **Ciltacel (Braun et al.)** | [Braun et al.](https://www.nature.com/articles/s41591-025-03499-9) | Reverse engineered DNA sequence provided at [GitHub](https://github.com/fraunhofer-izi/Braun_et_al_2024/blob/main/code/wgs/realign_potential_insertions_segemehl/Ciltacel_CARpos_consensus_Braun_et_al.fasta) | Translated from reverse engineered DNA | Full reverse engineered vector sequence provided at [GitHub](https://github.com/fraunhofer-izi/Braun_et_al_2024/blob/main/code/wgs/realign_potential_insertions_segemehl/Ciltacel_CARpos_consensus_Braun_et_al.fasta) |
| **Idecel** | Patent *WO2021091978A1* | Sequence No. 10 | Sequence No. 9; translated from DNA | Sequence No. 36 |
| **Tisacel** | Patent *US 9,499,629 B2* | SEQ ID NO: 8 | SEQ ID NO: 12; translated from DNA | SEQ ID NO: 1 |
| **Axicel** | DrugBank: [Roberts et al.](https://doi.org/10.1080/10428194.2017.1387905) → [Kochenderfer et al.](https://doi.org/10.1097/CJI.0b013e3181ac6138) → GenBank *HM852952* | GenBank ID *HM852952* | Translated from DNA | _Not available_ |
| **Hu19-CD28Z** | [Brudno et al.](https://pubmed.ncbi.nlm.nih.gov/31959992/) → NCBI  *MN698642.1* | NCBI entry *MN698642.1* | Translated from DNA | _Not available_ |


## Annotations (gtf)

### CAR constructs 

For annotation, known nucleotide sequences of CAR construct parts were retrieved from NCBI, following this [schematic](../Resources/CAR-constructs/#fda-approved-car-t-cell-therapie). 

**Domains retrieved**:  
- CD28, CD3ζ, 41BB, CD8, CSF2RA  
- Accession numbers: `"NM_001378516.1", "NM_171827.4", "NM_001561.6", "NM_001410981.1", "NR_027760.3"`

**Fetched Sequences**:  
[`fetched_sequences.fasta`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/fetched_sequences.fasta?ref_type=heads)

Each CAR construct was aligned against the retrieved domain sequences using BLAST. When applicable, annotations were compared with the original source data (`annotation_from_nucleotide_seq.json`) and compiled into a `.gtf` file.

All CAR sequences were additionally translated into protein sequence, and screened for protein domains with [SMART](http://smart.embl-heidelberg.de/smart). Based on protein position of predicted domains, nucleotide sequences were extracted [`find_nucleotide_from_protein.py`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/find_nucleotide_from_protein.py?ref_type=heads) and also added to the Annotation file [`annotation_from_nucleotide_seq.json`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/annotation_from_nucleotide_seq.json?ref_type=heads).

- **Full Annotation Script**: [`get_annotations.py`](https://github.com/fraunhofer-izi/TODO/-/blob/1b1148904205e7c43620f96ab9d8ebc27f621b18/Resources/extracted_pages/get_annotations.py)
- **Annotation File**: [`annotation_from_nucleotide_seq.json`](https://github.com/fraunhofer-izi/TODO/-/blob/add-scripts-to-pipeline/Resources/extracted_pages/annotation_from_nucleotide_seq.json?ref_type=heads)

### Vector systems

For vector systems annotation was done using
the [Addgene online tool](https://www.addgene.org/analyze-
sequence/). Features within gtf ﬁle were deﬁned by using
”Feature Type” according to Addgene Feature Options labels.
Only the predicted ORF for the CAR construct was added. All
annotation information are provided in GTF format.