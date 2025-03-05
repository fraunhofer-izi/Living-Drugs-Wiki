---
hide:
  - navigation
  - toc
class: pipelines-page
---
# Pipelines
Various computational biology approaches can be used to study and optimise adoptive cellular immunotherapies. For example, single-cell multi-omics technologies enable the study of heterogeneity within immune cell populations, but also within the tumour sample. In combination with V(D)J sequencing of T or B cell receptors and profiling of cell surface protein expression, a more comprehensive understanding of the immune diversity and clonal expansion of the tumour cell can be achieved.
Since CAR T cells, as genetically engineered cells, are very different from normal cells, it is essential to ensure their safety and efficacy. One critical aspect is the monitoring of the integration sites of the inserted CAR gene, which can be achieved by integration site analysis. This technique allows precise mapping of the CAR transgene integration site and can be used to determine clonality or to assess the potential risk of secondary malignancies. 
As CAR T-cell therapies continue to expand, careful monitoring and tailored computational approaches will be essential for refining these treatments and for advancing other emerging therapies such as T-cell receptor (TCR) therapy and natural killer (NK) cell-based therapies. In light of this, we provide tailored **pipelines** for the study and optimisation of adoptive cellular immunotherapies, with a focus on CAR T-cell therapy.

## Explore the Pipelines

<div class="grid cards" markdown>

-   __:microscope: LivingDrugOmics__

    ---

    - _Purpose:_ Multi-omics single-cell pipeline for CAR T cell profiling
    - _Supports_:
        - Automatic pipeline which supports 10x Genomics single-cell technologies such as gene expression (5' and 3'),  VDJ-T, VDJ-B, cell surface protein detection
        - Includes CAR-specific detection and quality control
    - _Output:_
        - Seurat object with integrated single-cell multi-omic RNA-seq data for downstream analysis

    [:arrow_right: LivingDrugOmics](../Pipelines/LivingDrugOmics-Pipeline/index.md)

-   __:computer: LivingDrugSpace (in-progress)__

    ---

    Here we will provide a nextflow pipeline which processes spatial transcriptomics data produced by Visium (HD). 

    [:arrow_right: Coming Soon]()

-   __:computer: Integration Site Analysis (in-progress)__

    ---

    ![Integration Site](../../uploads/ISA.png)
    
    [:arrow_right: Coming Soon]()

</div>

---

[Visit our GitHub Repository 🚀](https://github.com/fraunhofer-izi)
