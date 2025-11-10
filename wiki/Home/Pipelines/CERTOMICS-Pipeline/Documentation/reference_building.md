# Reference Building

!!! info
    To understand how the parameters are defined and used, take a look at the decision-making process: [reference_building](../../../../images/pipelines/CERTOMICS/Pipeline_options.drawio.svg)

## When is a reference built?

Depending on the input parameters, the process checks whether a gene expression reference has already been built or needs to be built on the fly. If a prebuilt reference is available and the `--gene_expression_reference` parameter is set, the process uses it and skips reference generation. Otherwise, the pipeline proceeds to build a new reference based on the provided input.

## How does the build process work?

The reference-building process is based on the pre-build scripts of the official 10x Genomics human references for [2024](https://www.10xgenomics.com/support/software/cell-ranger/downloads/cr-ref-build-steps#human-ref-2024-a) and [2020](https://www.10xgenomics.com/support/software/cell-ranger/downloads/cr-ref-build-steps#human-ref-2020-a). Both modified scripts can be found in the `templates` directory. They have been adapted for use in a Nextflow process but can still be reviewed manually.

### Input

There are 7 parameters involved in building a custom reference:

- `gene_expression_source_fa: <path>`
- `gene_expression_source_gtf: <path>`
- `gene_expression_source_fa_url: <map>`
- `gene_expression_source_gtf_url: <map>`
- `gene_expression_reference_version: <'2020'/'2024'>`
- `gene_expression_car_fa: <path>`
- `gene_expression_car_gtf: <path>`

To build a reference at least a Sequence file (FASTA / `.fa`) and an Annotation file (GTF / `.gtf`) are needed. The source files can be defined using the `gene_expression_source_fa` and `gene_expression_source_gtf` parameters. If they are not defined they have to be downloaded at runtime.  This is done using the URLs defined with the `gene_expression_source_fa_url` and `gene_expression_source_gtf_url` parameters.

!!! attention
    The provided source files (.fa and .gtf) should match those used in the 10x 2020/2024 reference builds, as the scripts include version-specific filtering steps. If users wish to use other references than those from 10x, they must build the reference themselves and provide it via the `gene_expression_reference` parameter.

If you wish to concatenate a CAR construct as well you also need the CAR Sequence file defined with the `gene_expression_car_fa` parameter as well as the CAR Annotation file defined with the `gene_expression_car_gtf` parameter. 

The `gene_expression_reference_version` parameter is used to decide which URL and what build script version is actually used in the process. It can either be `'2020'` or `'2024'` and defaults to `'2024'`. This means that the template `templates/build_reference_2024.sh`.

### Process

If either of the source files is not already provided, they are downloaded in the `GET_GEX_SOURCE` process. These files are then passed to `BUILD_GEX_REFERENCE`. If CAR files are defined, they are also included as inputs.

Within the build process, the appropriate script template is selected based on the `gene_expression_reference_version` parameter. The official 10x scripts are modified to additionally concatenation of CAR files — if provided — into the source files, just before the reference is built using `cellranger mkref`.