# Pipeline Configuration and Execution

This document describes how to configure and run the pipeline, including both command-line arguments and input parameters.

You can configure the pipeline in two main ways:

1. Command-line arguments provided directly when running `nextflow run`.
2. Params-file (`.yaml` or `.json`): a structured input file specifying all required parameters and options.

In practice, both approaches can be combined: command-line flags override values from the params-file. Using a params-file can be convenient for documentation purposes and reproducibility, though.

## Command-Line Arguments

When launching the pipeline, several command-line options are available to control execution. Except for Nextflow-specific arguments (those starting with a single `-`), all pipeline parameters can also be defined in the params-file.

Example:

```bash
nextflow run main.nf -profile singularity,slurm --outdir results --skip_qc
```

### Profiles

Profiles customize how the pipeline executes, for example, to run locally, on HPC systems, or within containers. You can specify one or more profiles using the `-profile` flag:

```bash
nextflow run main.nf -profile <profile1>,<profile2>
```

Available predefined profiles:

#### `singularity`

Runs all processes inside Singularity containers to ensure reproducibility and consistent environments. Containers are automatically pulled at runtime. Using this profile is highly recommended for production and reproducibility.

#### `slurm`

Executes processes on a Slurm-managed HPC cluster. Nextflow manages job submission, but you may need to adjust the default resource settings defined in the `nextflow.config` file to fit your environment.

#### `standard`

Runs the pipeline locally (default) without containers. All required binaries must be available in `$PATH`.

You can also define your own profiles in the `nextflow.config` file. See the [Nextflow documentation on profiles](https://www.nextflow.io/docs/latest/config.html#config-profiles) for details.

## The Params File

User input is usually provided as a `.yaml` or `.json` file referred to as the **params-file**. It defines input data, references, and pipeline behavior. A params-file enables reproducible and organized configuration. This is especially useful for routine use or large analyses.

### Pipeline Mode

Use the `pipeline_mode` parameter to control which parts of the pipeline are executed:

- `full`: Run full pipeline with all steps (default)
- `reference`: Only build custom references
- `analysis`: Run only analysis and QC steps

### References

#### Gene Expression

A Gene Expression reference can be provided as either prebuilt files or built dynamically at runtime. If you’re interested in how references are constructed, see [reference_building.md](./reference_building.md).

**Prebuilt reference:**

```yaml
gene_expression_reference: '/path/to/gex/reference'
```

**Or build dynamically:**

```yaml
gene_expression_source_fa: '/path/to/genome.fa'
gene_expression_source_gtf: '/path/to/annotation.gtf'
gene_expression_car_fa: '/path/to/CAR.fa'      # optional
gene_expression_car_gtf: '/path/to/CAR.gtf'    # optional
gene_expression_reference_version: '2024'      # default: '2024'
```

The `gene_expression_car_fa` and `gene_expression_car_gtf` parameters are used when building a **custom reference (e.g., for detection of CAR mapping reads)**, as they are concatenated with their source counterparts if set. However, they are not simply ignored when `gene_expression_reference` is set. This is useful if you have a prebuilt custom reference with a concatenated CAR construct because in order for the pipeline to build metrics around the CAR construct, it needs the unconcatenated construct as well.

**For a visual explanation**, see the [decision tree](../../../../images/pipelines/CERTOMICS/Pipeline_options.drawio.svg).

#### V(D)J

```yaml
vdj_reference: '/path/to/vdj/reference'
```

#### Feature Barcoding

```yaml
feature_reference: '/path/to/feature/reference'
```

Only references relevant to your libraries need to be provided.

## Samplesheet

Sample information is passed via a YAML file using the `samplesheet` parameter. Each sample consists of the attributes `name` and `libraries`. The `name` attribute is an identifier for the sample and is used when naming the output. `libraries`, on the other hand, is, again, a list of maps. Each entry in `libraries` represents a 10x Genomics library and must include the fields `fastq_path`, `fastq_id`, and `feature_types`. These fields correspond to the [definitions used by Cell Ranger Multi](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-multi-config-csv-opts#libraries). The content of a sample sheet file might look like this:

```yaml
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

### Quality Control (QC) Options

You can selectively skip quality control steps using the following flags:

- `--skip_fastqc`: Skip FastQC
- `--skip_fastq_screen`: Skip FastQ Screen
- `--skip_multiqc`: Skip MultiQC
- `--skip_qc`: Skip **all** QC steps

### Miscellaneous Settings

Common configurable parameters and their default values:

```yaml
outdir: "${projectDir}/output"
trace_report_suffix: "{yyyy-MM-dd_HH-mm-ss}"
validate_params: true
```

## Experimental features

CellRanger allows you to use a job scheduler like Slurm to distribute the subprocesses spawned by their pipelines. This can be used to significantly reduce runtime of the slow `CELLRANGER_MULTI` process. This feature is experimental and may cause pipelines running indefinitely without failing or processes being killed prematurely. For more information about cluster mode read [the support article about job submission mode](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-job-submission-mode) and [the support article about cluster mode](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-cluster-mode).

- `cellranger_disable_ui` - Flag to disable the Web-UI provided by the CellRanger processes (Safe to use)
- `cellranger_enable_cluster` - Flag to enable cluster mode
- `cellranger_cluster_template` - Path to a `.template` file for your respective workload manager - default: `assets/cluster_templates/slurm.template`
- `cellranger_max_jobs` - Maximum amount of jobs that can be spawned by a single instance of the CellRanger process - default: 4
- `cellranger_mem_per_core` - Maximum amount of memory consumed per CPU

### Example Params Files

**Example 1: Using Prebuilt References**

```yaml
gene_expression_reference: '/path/to/gex/reference'
vdj_reference: '/path/to/vdj/reference'
feature_reference: '/path/to/feature/reference'
samplesheet: '/path/to/samplesheet.yaml'
```

**Example 2: Building a Custom Reference**

```yaml
gene_expression_source_fa: '/path/to/gex/source.fa'
gene_expression_source_gtf: '/path/to/gex/source.gtf'
gene_expression_car_fa: '/path/to/gex/car.fa'
gene_expression_car_gtf: '/path/to/gex/car.gtf'
feature_reference: '/path/to/feature/reference'
pipeline_mode: 'reference'
```
