# Reference Building

## When is a reference built?

A gene expression reference is only needed when a gene expression library is present. If no gene expression library is used, then a reference is not required, and the process is skipped. If a gene expression library is used, the next step is to check whether a gene expression reference has already been provided. If a prebuilt reference is available, there is no need to generate a new one, and the process stops. However, if no reference is provided, the pipeline proceeds to build one based on the input parameters.

## How does the build process work?

The reference building process is based on the build scripts of the official 10x human references for [2024](https://www.10xgenomics.com/support/software/cell-ranger/downloads/cr-ref-build-steps#human-ref-2024-a) and [2020](https://www.10xgenomics.com/support/software/cell-ranger/downloads/cr-ref-build-steps#human-ref-2020-a). Both modified scripts can be found in the `templates` directory. They are modified to be used by a Nextflow process but can still be looked at.

### Input

There are 7 parameters that come into play when building a custom reference. 

- `gene_expression_source_fa: <path>`
- `gene_expression_source_gtf: <path>`
- `gene_expression_source_fa_url: <map>`
- `gene_expression_source_gtf_url: <map>`
- `gene_expression_reference_version: <'2020'/'2024'>`
- `gene_expression_car_fa: <path>`
- `gene_expression_car_gtf: <path>`

To build a reference at least a Sequence file (FASTA / `.fa`) and an Annotation file (GTF / `.gtf`) are needed. The source files can be defined using the `gene_expression_source_fa` and `gene_expression_source_gtf` parameters. If they are not defined they have to be downloaded at runtime. This is done using the URLs defined with the `gene_expression_source_fa_url` and `gene_expression_source_gtf_url` parameters.

If you wish to concatenate a CAR construct as well you also need the CAR Sequence file defined with the `gene_expression_car_fa` parameter as well as the CAR Annotation file defined with the `gene_expression_car_gtf` parameter. 

The `gene_expression_reference_version` parameter is used to decide which URL and what build script version is actually used in the process. It can either be `'2020'` or `'2024'` and defaults to `'2024'`. This means that the template `templates/build_reference_2024.sh`.

### Process

If at least one of the source files are not provided already they are downloaded in the `GET_GEX_SOURCE` process. From there they are used as an input for the `BUILD_GEX_REFERENCE`. If both are set the CAR-files are also used as input for the process. In the process itself the template is selected based on the `gene_expression_reference_version` parameter. The only real change done to the 10x build scripts is to, if staged, concatenate the CAR-files to the source files right before the reference is built using `cellranger mkref`. 
