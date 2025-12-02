# Available parameters

The arguments described here can also be found when running the pipeline with the `--help` flag.



## Quality Control

If desired, it is possible to skip the Quality Control (QC) steps (or individual subprocesses) during the pipeline execution. The following flags are available for skipping specific QC steps:

- `--skip_fastqc` - Flag to skip FastQC

- `--skip_fastq_screen` - Flag to skip FastQ Screen

- `--skip_multiqc` - Flag to skip MultiQC

- `--skip_qc` - Flag to skip all QC steps entirely

## Config files

The `MULTIQC` process need a configuration file to run properly. By default, the config file defined in `assets/config` is used but they can be changed with its respective parameter

- `--multiqc_config <path>`

## Experimental features

CellRanger allows you to use a job scheduler like Slurm to distribute the subprocesses spawned by their pipelines. This can be used to significantly reduce runtime of the slow `CELLRANGER_MULTI` process. This feature is experimental and may cause pipelines running indefinitely without failing or processes being killed prematurely. For more information about cluster mode read [this](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-job-submission-mode) and [this](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-cluster-mode).

- `--cellranger_disable_ui` - Flag to disable the Web-UI provided by the CellRanger processes (Safe to use)
- `--cellranger_enable_cluster` - Flag to enable cluster mode
- `--cellranger_cluster_template <path>` - Path to a `.template` file for your respective workload manager - default: `assets/cluster_templates/slurm.template`
- `--cellranger_max_jobs` - Maximum amount of jobs that can be spawned by a single instance of the CellRanger process - default: 4
- `--cellranger_mem_per_core` - Maximum amount of memory consumed per CPU
