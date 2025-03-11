# User Input - The Params File
User input is primarily passed as a `.yaml` or `.json` file containing the required parameters. This file is referred to as the `params-file`. Normally, the parameters in the file are listed in a flat structure without branches.

As this pipeline supports the analysis of common 10x Genomics libraries for single-cell (immune profiling) by using CellRanger Multi, please refer to the original website for more information: [Cell Ranger multi 3'](https://www.10xgenomics.com/support/software/cell-ranger/latest/analysis/running-pipelines/cr-3p-multi) and [Cell Ranger multi 5' immune profiling](https://www.10xgenomics.com/support/software/cell-ranger/latest/analysis/running-pipelines/cr-5p-multi).

## References
The references are provided through a series of different parameters. If you are interested in how the reference is built, read [this](../Documentation/reference_building.md)

Gene Expression:

- `gene_expression_reference: <path>` - A prebuilt 10xGenomics compatible gene expression reference.

- `gene_expression_reference_version: <'2020'/'2024'>` - Version of the reference building script to use - default: `'2024'`

- `gene_expression_source_fa: <path>` - Genome to build the custom gene expression reference with at runtime.

- `gene_expression_source_gtf: <path>` - Annotation to build the custom gene expression reference with at runtime.

- `gene_expression_car_fa: <path>` - CAR genome to add to gene expression reference at runtime.

- `gene_expression_car_gtf: <path>` - CAR annotation to add to gene expression reference at runtime.

VDJ:

- `vdj_reference: <path>` - A prebuilt 10xGenomics compatible VDJ reference.

Feature Barcoding:

- `feature_reference: <path>`: A prebuilt 10xGenomics compatible feature reference.

These parameters can be put into the config like this:

```yaml
gene_expression_reference: '/path/to/gex/reference'
vdj_reference: '/path/to/vdj/reference'
feature_reference: '/path/to/feature/reference'
```

Note that only the references that will actually be used are necessary. For instance, if no gene expression library is used, there is no need to provide a gene expression reference. 

Regarding the `gene_expression_*` parameters, it is important to understand that the behavior of the pipeline changes depending on the parameters provided. This is because the pipeline can build a gene expression reference at runtime if the appropriate files are provided (at least `gene_expression_source_fa` and `gene_expression_source_gtf`). If `gene_expression_reference` is set then the parameters `gene_expression_source_fa` and `gene_expression_source_gtf` are ignored, as it would be unnecessary to build a new reference if a pre-built reference is provided. The `gene_expression_car_fa` and `gene_expression_car_gtf` parameters also come into play when building a **custom reference (e.g. for detection of CAR mapping reads)**, as they are concatenated with their source counterparts if set. However, they are not simply ignored when `gene_expression_reference` is set. This is useful if you have a prebuilt custom reference with a concatenated CAR construct because in order for the pipeline to build metrics around the CAR construct it needs the unconcatenated construct. To do this just provide both `gene_expression_reference` as well as `gene_expression_car_fa` and `gene_expression_car_gtf`.

## Samples

Unlike other parameters, the `samples` parameter is a list of maps. Each sample consists of the attributes `name` and `libraries`. The `name` attribute is an identifier for the sample and is used when naming the output. `libraries`, on the other hand, is, again, a list of maps. Each entry in `libraries` represents a 10x Genomics library and must include the fields `fastq_path`, `fastq_id`, and `feature_types`. These fields correspond to the [definitions used by Cell Ranger Multi](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-multi-config-csv-opts#libraries). When compiled, the value of `samples` might look like this:

```yaml
samples:
  - name: 'sample_1'
    libraries:
      - fastq_id: 'sample_1_R'
        fastqs: '/path/to/sample1'
        feature_types: 'Gene Expression'
      - fastq_id: 'sample_1_B'
        fastqs: '/path/to/sample1'
        feature_types: 'VDJ-B'
      - ...
  - name: ... 
```

Currently, only the feature types `Gene Expression`, `VDJ-T`, `VDJ-B` and `Antibody Capture` are supported.

## Miscellaneous settings
For this pipeline, the params-file is primarily used to supply input to the pipeline, but it is not limited to just that. Settings like the output directory can also be overridden here instead of using command line arguments. Here is a short list of common settings and their default values:

```yaml
outdir: "${projectDir}/output"
skip_qc: false
skip_multiqc: false
trace_report_suffix: "{Current date (yyyy-MM-dd_HH-mm-ss)}"
validate_params: true
```

Read [this](./cli.md) if you want to learn more about the supported arguments.

## Params-File Examples

```yaml
gene_expression_reference: '/path/to/gex/reference'
vdj_reference: '/path/to/vdj/reference'
feature_reference: '/path/to/feature/reference'
samples:
  - name: 'sample_1'
    libraries:
      - fastq_id: 'sample_1_R'
        fastqs: '/path/to/sample1'
        feature_types: 'Gene Expression'
      - fastq_id: 'sample_1_T'
        fastqs: '/path/to/sample1'
        feature_types: 'VDJ-T'
      - fastq_id: 'sample_1_B'
        fastqs: '/path/to/sample1'
        feature_types: 'VDJ-B'
      - fastq_id: 'sample_1_A'
        fastqs: '/path/to/sample1'
        feature_types: 'Antibody Capture'
  - name: ...
```

```yaml
gene_expression_source_fa: '/path/to/gex/source.fa'
gene_expression_source_gtf: '/path/to/gex/source.gtf'
gene_expression_car_fa: '/path/to/gex/car.fa'
gene_expression_car_gtf: '/path/to/gex/car.gtf'
feature_reference: '/path/to/feature/reference'
samples:
  - name: 's1'
    libraries:
      - fastq_id: 'GEX_s1'
        fastqs: '/path/to/GEX_s1'
        feature_types: 'Gene Expression'
      - fastq_id: 'ADT_s1'
        fastqs: '/path/to/ADT_s1'
        feature_types: 'Antibody Capture'
```
