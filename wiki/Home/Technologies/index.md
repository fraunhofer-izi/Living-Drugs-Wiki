---
hide:
  - navigation
  - toc
---
# Technologies for adoptive immunotherapies
## Multi-omics single cell sequencing
Multi-omics single-cell sequencing from 10x Genomics integrates various layers of biological data, such as transcriptomics (RNA), immune repertoire profiling, chromatin accessibility, and surface protein expression, all within individual cells. In adoptive immunotherapies like CAR-T cells, this technology allows researchers to simultaneously analyze how these multiple modalities interact, providing a comprehensive view of T-cell behavior. Key benefits include:

  - **5’ and 3’ single-cell RNA sequencing**: These methods capture either the 5’ or 3’ ends of mRNA transcripts, revealing gene expression profiles with high resolution. In CAR-T cell therapy, this can uncover activation states, cytokine production, and tumor-antigen responses, as well as heterogeneity within CAR-T populations.

  - Immune profiling: 10x Genomics' Single Cell Immune Profiling platform enables simultaneous analysis of gene expression and **T-cell receptor (TCR) or B-cell receptor (BCR) sequences**, providing insights into immune cell clonality, diversity, and receptor specificity. This allows precise tracking of CAR-T cells, mapping out clonal dynamics, exhaustion states, and functional markers critical for therapeutic success. It further enables profiling of **surface protein expression**, via feature barcodes. Those protein markers complement gene expression markers for cell-specific profiling.


## Spatial sequencing
Spatial sequencing technologies, such as Visium and Visium HD by 10x Genomics, map gene expression profiles to their specific locations within tissue samples. By preserving spatial context, these technologies provide critical insights into how immune cells interact with tumors, offering a more comprehensive understanding of therapy efficacy. This information can help refine CAR-T cell therapies by identifying factors that influence their success or resistance within the tumor microenvironment. 

## Custom Probes for CAR detection
We have developed custom probes for robust detection of Carvykti in Visium (HD) spatial transcriptomics. The probe design was based on the specifications of the technical note “CG000621” from 10xGenomics. The positioning of the probes within the chimeric CAR construct was chosen to span the boundaries of the cloned domains, resulting in unique sequences that were inserted into the Visium Probe Set v1 for data analysis. For more information please contact: Blumert, Conny <conny.blumert@izi.fraunhofer.de>
