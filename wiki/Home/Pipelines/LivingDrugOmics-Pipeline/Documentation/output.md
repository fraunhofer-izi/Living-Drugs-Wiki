# Output

## Where to Find Output
The output directory can be set using the `outdir` parameter. If this parameter is not overridden using the [params-file](./params-file.md) or [command-line arguments](./cli.md), the output is written to `${projectDir}/output`.

## Output Structure
After the pipeline completes successfully, the output directory should contain the following subdirectories:

??? note "Gene Expression Reference"
    The `gene_expression_reference` directory contains the output of the `BUILD_GEX_REFERENCE` process, which is run when building a reference at runtime. Using this output instead of regenerating the reference for each pipeline run helps reduce runtime and computing power.

### Analysis Results 

??? note "CellRanger Multi"
    The `cellranger_multi` directory contains per-sample output directories from the `CELLRANGER_MULTI` process.

??? note "Seurat Object"
    The `seurat_object` directory contains the output of the `SEURAT_OBJECT` process, specifically the Seurat object itself. A merged Seurat object (`seurat_merged.Rds`) is generated, which includes all samples and their respective data types from 10x Genomics libraries.

    Gene expression data is stored in an assay called "RNA," while Antibody Capture data is stored in an additional assay called "ADT."

    Additional metadata includes quality scores, mitochondrial and ribosomal gene abundance, cell cycle scores, and doublet removal information.

    #### Metadata Fields

    **General Information**
    - `orig.ident`: Original identity or batch identifier for each sample.
    - `nCount_RNA`: Total RNA molecule counts (UMI counts) for each cell.
    - `nFeature_RNA`: Number of unique genes detected in the RNA assay for each cell.
    - `nCount_ADT`: Total counts for the Antibody-Derived Tag (ADT) assay.
    - `nFeature_ADT`: Number of unique features detected in the ADT assay.

    **Doublet Removal Scores (calculated with scDblFinder)**
    - `scDblFinder_score`: Score estimating the likelihood that a cell is a doublet.
    - `scDblFinder_class`: Classification of cells as "singlet" or "doublet".

    **Cell Cycle Information**
    - `S.Score`: Score representing the activity of the S phase calculated with Seurat CellCycleScoring().
    - `G2M.Score`: Score representing the activity of the G2/M phase calculated with Seurat CellCycleScoring().
    - `Phase`: Predicted cell cycle phase (G2M, S or G1) based on S.Score and G2M.Score
    - `CellCycle`: True if cycling else False. Calculated using a cluster-based enrichement method. Enrichment based on genes from cell.cycle.obj of ProjectTILs package.
    - `CellCycle_Phase`: Combined Cell Cycle information based on CellCycleScoring() and Cluster-based apprach using gene set enrichment.
    

    **Clonality and VDJ Information (if available)**
    - `CTgene`: Clonotype gene information for each cell.
    - `CTnt`: Nucleotide sequence information of the clonotype.
    - `CTaa`: Amino acid sequence information of the clonotype.
    - `clonalProportion`: Proportion of cells belonging to a given clonotype.
    - `clonalFrequency`: Frequency of a specific clonotype in the sample.
    - `cloneSize`: Clonotype size category (e.g., "Single," "Small," "Medium," "Large," or "Hyperexpanded").

??? note "Quarto Webpage Summary"
    The `quarto` directory contains an **interactive webpage** that summarizes **cross-sample quality metrics**, allowing for **direct comparisons** between different samples. This summary includes:

    - CAR-specific quality control metrics
    - GEX-specific metrics
    - VDJ-specific metrics

    #### CAR-Specific Quality Control Metrics

    **Read-Level Metrics**
    - Coverage (unique and multimapping reads) across the CAR construct.
    - Absolute read counts against CAR construct per sample.

    **Count-Level Metrics**
    - Percentage (and absolute numbers) of CAR-positive cells (count>0) compared to all T cells (CD4, CD8, gd) (based on scGate annotation) per sample.
    - Percentage (and absolute numbers) of CAR-positive cells (count>0) compared to all CD4+ (A) and CD8+ (B) T cells (scGate annotation PBMC model) per sample.

    #### GEX-specific Metrics

    **Cell Proportions**
    - Insight into the distribution of different cell types, predicted with scGate using the PBMC model and default parameters.

    #### VDJ-specific Metrics

    **Clonotype composition for T and B cell receptor data**: Absolute and relative numbers of unique clonotypes per sample.

### QC  

??? note "FastQC"
    The `fastqc` directory contains the per-sample output directories from the `FASTQC` processes, containing a FastQC report for each sample.

??? note "FastQ Screen"
    The `fastq_screen` directory contains the per-sample output directories from the `FASTQ_SCREEN` processes, including a report verifying whether sequencing runs contain expected sequences by testing against genomes in `assets/fastq_databases`.

??? note "MultiQC"
    The `multiqc` directory contains the output of the `MULTIQC` process, which provides a summary of FastQC and FastQ Screen results.

??? note "Pipeline Info"
    The `pipeline_info` directory contains log data from the Nextflow pipeline itself.