# LivingDrugOmics
<div class="grid cards" markdown>
-   __:rocket: Getting started__

    ---
    If you're only interested in how to use the pipeline and its inputs, head over to the quickstart guide. 

    [:arrow_right: Get started quickly](#quickstart-guide)

-   __:book: What is LivingDrugOmics__

    ---
    Want to understand what LivingDrugOmics is and how it works?

    [:arrow_right: What is LivingDrugOmics](#what-is-livingdrugomics)
    [:arrow_right: Code documentation](#basic-code-documentation)
</div>

# What is LivingDrugOmics
This Nextflow pipeline has been developed to support **single-cell multi-omics** for in-depth profiling of current **CAR T-cell** products. LivingDrugOmics enables thereby comprehensive immune profiling by supporting single-cell 10x Genomics technologies, such as gene expression (GEX) sequencing, cell surface protein detection, and V(D)J sequencing. Specific quality control metrics are incorporated for robust identification of CAR-positive cells.

![Abb_CAR_T_cell_profiling.png](../../../uploads/Abb_CAR_T_cell_profiling.png){.half-size}

In addition, available sequence and annotation data on CAR constructs and vector systems are collected in our GitHub [repository](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/tree/main/Resources?ref_type=heads). This serves as a scientific [resource](../../Resources/index.md) and is designed to support the analysis and development of CAR T-cell therapies.

## Single-cell multi-omics
The _LivingDrugOmics_ pipeline enables comprehensive immune profiling by supporting single-cell 10x Genomics technologies, such as gene expression (GEX) sequencing, cell surface protein detection, and V(D)J (TCR and BCR) sequencing. To reliably identify CAR+ cells, the pipeline is provided with a custom CAR reference, enabling the detection and characterisation of CAR-positive cells.

## Pipeline Overview
- `Workflow: HANDLE_REFERENCES` - Depending on the libraries used (GEX, VDJ, ADT) and the CAR construct (FASTA, GTF), a custom gene expression reference (for CellRanger) can be created.
- `Workflow: RUN_SECONDARY_ANALYSIS` - Executes CellRanger Multi-analysis and generates a merged, annotated Seurat object as well as CAR specific metrics.
- `Workflow: RUN_QUALITY_CONTROL` - Quality control is performed using FastQC and FastQ-Screen. The results are merged using MultiQC.

![DAG Graph](../../../images/LivingDrugOmics/pipeline_dag/general_pipeline_dag.drawio.svg){.half-size}

## Seurat Object Output
The output of this pipeline is a merged Seurat object containing multi-modal single-cell data (RNA, VDJ and ADT assays) along with extensive metadata on cell type identity, quality metrices, cell cycle, and clonotype information, which serves the purpose of enabling detailed characterization, classification, and quality assessment of diverse cell populations from multiple samples. For a detailed explanation please see: [Seurat Output](Usage/03_Output.md#seurat-object)

## Quality control
Specific quality control metrics are incorporated for quality control of single-cell data ([MultiQC](https://seqera.io/multiqc/)) and robust identification of CAR-positive cells.

### Multi-QC Report
Provides an overview of general quality metrics via [FastQ-Screen](https://www.bioinformatics.babraham.ac.uk/projects/fastq_screen/) and [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/):

### CAR-specific Metrics
CAR-specific metrics include quality controls based on reads mapping to the specific CAR construct and Cellranger raw counts, including the percentage of CAR+ cells of all annotated T cells. Annotation is performed using the [scGate tool](https://academic.oup.com/bioinformatics/article/38/9/2642/6544581) with the PBMC model, ensuring identification and characterization of CAR+ T cell populations and other cell types.

![CAR__metrics](../../../images/LivingDrugOmics/CAR-QC-1.png)

# Quickstart guide
## Downloading the pipeline
To install the pipeline, simply download the Git repository via HTTP.

```sh
git clone https://github.com/fraunhofer-izi/TODO.git
```

Before attempting to run the pipeline, ensure that Nextflow is installed and up-to-date (`version >= 24.10.2`). If you use the pipeline with the Singularity container (recommended via`-profile sigularity`), Singularity must be installed and included in PATH, as well.

## Supplying data
To provide all the necessary data (references, samples, etc.) a separate file is used. All values are captured in the YAML (or JSON) format in a so-called parameters file (or params-file) and passed to the pipeline with the `-params-file` flag.
The parameters file should look something like this:

```YAML
gene_expression_reference: "/path/to/gex/reference"
vdj_reference: "/path/to/vdj/reference"
samples:
  - name: 'sample_1'
    libraries:
      - fastq_id: 'sample_1_R'
        fastqs: "/path/to/sample_1_R"
        feature_types: 'Gene Expression'
      - fastq_id: 'sample_1_B'
        fastqs: "/path/to/sample_1_B"
        feature_types: 'VDJ-B'
```

A full explanation of the options you have and how to populate your own params-file can be found [here](Usage/01_Userinput-The-Params-File.md).

## Diving deeper
To get a better understanding of what you can do with the pipeline and the options you have, check out the documentation

- [Params-file](Usage/01_Userinput-The-Params-File.md) with examples
- [Command line arguments](Usage/02_Command-Line-Arguments.md)
- [Pipeline output](Usage/03_Output.md)

# Basic code Documentation
To make the code easier to understand we added brief explanations for each script file.

- [main.nf](Documentation/main.md)
- [workflows/handle_references](Documentation/handle_references.md)
- [workflows/initiate_pipeline.nf](Documentation/initiate_pipeline.md)
- [workflows/quality_control.nf](Documentation/quality_control.md)
- [workflows/secondary_analysis.nf](Documentation/secondary_analysis.md)
