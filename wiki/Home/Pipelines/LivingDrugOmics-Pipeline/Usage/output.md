# Output

## Where to Find Output
The output directory can be set using the `outdir` parameter. If this parameter is not overridden using the [params-file](./params-file.md) or [command-line arguments](./cli.md), the output is written to `${projectDir}/output`.

## Output Structure
After the pipeline completes successfully, the output directory should contain the following subdirectories:

- `gene_expression_reference`

- `cellranger_multi`

- `seurat_object`

- `quarto`

- `fastqc`

- `fastq_screen`

- `multiqc`

- `pipeline_info`

Each directory contains the output from its respective process. Per-sample processes are organized into subdirectories named after each sample.

## Logging
The `pipeline_info` directory contains log data from the Nextflow pipeline itself.

## Quality Control Results

### FastQC
The `fastqc` directory contains the per-sample output directories from the `FASTQC` processes, containing a FastQC report for each sample.

### FastQ Screen
The `fastq_screen` directory contains the per-sample output directories from the `FASTQ_SCREEN` processes, including a report verifying whether sequencing runs contain expected sequences by testing against genomes in `assets/fastq_databases`.

### MultiQC
The `multiqc` directory contains the output of the `MULTIQC` process, which provides a summary of FastQC and FastQ Screen results.

## Analysis Results

### Gene Expression Reference
The `gene_expression_reference` directory contains the output of the `BUILD_GEX_REFERENCE` process, which is run when building a reference at runtime. Using this output instead of regenerating the reference for each pipeline run helps reduce runtime and computing power.

### CellRanger Multi
The `cellranger_multi` directory contains per-sample output directories from the `CELLRANGER_MULTI` process.

### Quarto
TODO

### Seurat Object
The `seurat_object` directory contains the output of the `SEURAT_OBJECT` process, specifically the Seurat object itself. A merged Seurat object (`seurat_merged.Rds`) is generated, which includes all samples and their respective data types from 10x Genomics libraries.

Gene expression data is stored in an assay called "RNA," while Antibody Capture data is stored in an additional assay called "ADT."

Additional metadata includes quality scores, mitochondrial and ribosomal gene abundance, cell cycle scores, and doublet removal information.

Here is a complete list of all metadata information:

#### General Information

- **`orig.ident`**  
    - **Type**: Factor  
    - Description: The original identity or batch identifier for each sample.

- **`nCount_RNA`**  
    - **Type**: Numeric  
        - Description: The total RNA molecule counts (UMI counts) for each cell.

- **`nFeature_RNA`**  
    - **Type**: Integer  
        - Description: The number of unique genes detected in the RNA assay for each cell.

- **`nCount_ADT`**  
    - **Type**: Numeric  
        - Description: The total counts for the Antibody-Derived Tag (ADT) assay for each cell.

- **`nFeature_ADT`**  
    - **Type**: Integer  
        - Description: The number of unique features (protein markers) detected in the ADT assay for each cell.

#### Doublet Removal Scores

- **`scDblFinder_score`**  
    - **Type**: Numeric  
        - Description: The score estimating the likelihood that a cell is a doublet.

- **`scDblFinder_class`**  
    - **Type**: Factor  
        - Description: Classification of cells by `scDblFinder` as either "singlet" or "doublet".

#### Annotation Based on Raw Counts

- **`CD4CD8_BY_EXPRS`**  
    - **Type**: Factor  
        - Description: Annotation based on CD4/CD8 gene expression for T cell subtypes.

- **`CD3_BY_EXPRS`**  
    - **Type**: Factor  
        - Description: Annotation based on CD3 gene expression, typically identifying T cells.

- **`CAR_BY_EXPRS`**  
    - **Type**: Factor  
        - Description: Annotation of CAR-T cells based on chimeric antigen receptor (CAR) expression.

#### UCell Enrichment Scores (scGate-Based Annotation)

- **`<CellType>_UCell`**  
    - **Type**: Numeric  
        - Description: UCell enrichment scores for various cell types, indicating gene set activity associated with immune or stromal cell types. Examples include:
            - `Immune_UCell`
            - `Lymphoid_UCell`
            - `Tcell_UCell`
            - `Bcell_UCell`
            - `Myeloid_UCell`
            - `Macrophage_UCell`
            - `NK_UCell`
            - `Fibroblast_UCell`
            - `Epithelial_UCell`, etc.

#### Cell Type Information from scGate

- **`is.pure_<CellType>`**  
    - **Type**: Logical  
        - Description: Boolean classification (TRUE/FALSE) indicating if a cell belongs to a particular cell type based on the `scGate` tool. Examples include:
            - `is.pure_Bcell`
            - `is.pure_CD4T`
            - `is.pure_CD8T`
            - `is.pure_NK`
            - `is.pure_Monocyte`, etc.

- **`scGate_multi`**  
    - **Type**: Factor  
        - Description: Multi-label classification generated by scGate, indicating the main cell types for each cell.

- **`CellOntology_name`**  
    - **Type**: Character  
        - Description: The cell ontology name assigned to each cell.

- **`CellOntology_ID`**  
    - **Type**: Character  
        - Description: The corresponding cell ontology ID for the assigned cell type.

### Data Quality of Cells Regarding Mitochondrial and Ribosomal Genes

- **`Perc_of_mito_genes`**  
    - **Type**: Numeric  
        - Description: The percentage of mitochondrial gene counts out of the total RNA counts.

- **`Perc_of_ribosomal_genes`**  
    - **Type**: Numeric  
        - Description: The percentage of ribosomal protein genes (RPL, RPS) out of the total RNA counts.

- **`log10GenesPerUMI`**  
    - **Type**: Numeric  
        - Description: Log10-transformed ratio of genes per UMI for each cell, assessing cell quality.

### Cell Cycle Information (Seurat::CellCycleScoring)

- **`S.Score`**  
    - **Type**: Numeric  
        - Description: Score representing the activity of the S phase of the cell cycle.

- **`G2M.Score`**  
    - **Type**: Numeric  
        - Description: Score representing the activity of the G2/M phase of the cell cycle.

- **`Phase`**  
    - **Type**: Factor  
        - Description: The predicted cell cycle phase (e.g., "G1", "S", "G2M").

- **`CellCycle`**  
    - **Type**: Factor  
        - Description: A binary annotation indicating whether the cell is actively cycling (TRUE/FALSE).

- **`CellCycle_Phase`**  
    - **Type**: Factor  
        - Description: Refined phase classification, such as "G1M," "S," or "G2M."

- **`CellCycle_SCORE_UCell`**  
    - **Type**: Numeric  
        - Description: UCell-based cell cycle score representing gene set enrichment for cell cycle-related genes.

#### Clonality and VDJ Information (if VDJ)

- **`CTgene`**  
    - **Type**: Character  
        - Description: The clonotype gene information for each cell, based on VDJ sequencing.

- **`CTnt`**  
    - **Type**: Character  
        - Description: The nucleotide sequence information of the clonotype for each cell.

- **`CTaa`**  
    - **Type**: Character  
        - Description: The amino acid sequence information of the clonotype for each cell.

- **`CTstrict`**  
    - **Type**: Character  
        - Description: A stricter version of the clonotype definition that matches TCR/BCR more stringently.

- **`clonalProportion`**  
    - **Type**: Numeric  
        - Description: The proportion of cells belonging to a given clonotype within the sample.

- **`clonalFrequency`**  
    - **Type**: Integer  
        - Description: The frequency of a specific clonotype in the sample.

- **`cloneSize`**  
    - **Type**: Factor  
        - Description: Clonotype size category based on abundance, with values such as "Single," "Small," "Medium," "Large," or "Hyperexpanded."
