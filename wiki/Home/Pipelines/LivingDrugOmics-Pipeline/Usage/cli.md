# Command Line Arguments
When launching the pipeline, several options are available to further configure the execution through command-line arguments. These settings (excluding Nextflow specific arguents starting with `-` instead of `--`) can also be defined in the [Params-file](./params-file.md), which could be used to document the execution more thoroughly. However, if you prefer to keep the params-file minimal, using command-line arguments is a valid approach.

## Available Arguments
### Profiles
Profiles are a powerful tool for customizing how the pipeline is executed. They can be used to adjust the environment, such as utilizing HPC systems or enabling containerization for processes. There are three preconfigured profiles `singularity`, `slurm`, and `standard` which can be enabled using the `-profile` flag when launching Nextflow. You can also combine multiple profiles like so: 

```sh
nextflow run ... -profile <profile1>,<profile2>,<...>
```

You can also define your own profiles by changing the `nextflow.config`. Read the [Nextflow documentation about profiles](https://www.nextflow.io/docs/latest/config.html#config-profiles) if you are interested in doing so.

#### Singularity
If you want the pipeline to use containers for its processes, ensuring consistent and reproducible results, the `singularity` profile is the way to go. Containers are pulled at runtime as needed, and they come prepackaged with all necessary dependencies for each process. Using the `singularity` profile is the recommended method as it provides consistency and avoids version conflicts.

#### Slurm
The `slurm` profile enables the pipeline to use the Slurm workload manager for distributing processes across a cluster environment. The actual distribution of processes is handled by Nextflow. However, note that the default resource values for processes may not work for your environment. Make sure to adjust them in the `nextflow.config` file accordingly.

#### Standard
The `standard` profile simply instructs Nextflow to run the pipeline locally, which is the default behavior. It also expects all required binaries to be in `$PATH` so no containers are used. This profile is enabled by default.

### Quality Control
If desired, it is possible to skip the Quality Control (QC) steps (or individual subprocesses) during the pipeline execution. The following flags are available for skipping specific QC steps:

- `--skip_fastqc` to skip FastQC

- `--skip_fastq_screen` to skip FastQ Screen

- `--skip_multiqc` to skip MultiQC

- `--skip_qc` to skip all QC steps entirely

### Config files
The processes `MULTIQC` and `FASTQ_SCREEN` need configuration files to run properly. By default they are using the files defined in `assets/config` but they can be changed with their respective parameters

- `--multiqc_config <path>`

- `--fastq_screen_config <path>`

Important: Working with FastQ-Screen databases within Nextflow can be tricky because you cannot access files outside of the project directory without staging them. Because you have to move the databases into the `assets/fastqs_databases` directory and reference them relative to the project directory with the `${projectDir}` variable which is substituted at runtime (Using other variables will not work). Check out the default config `assets/config/fastqs_config.conf` for an example.

### Experimental features

CellRanger allows you to use a job scheduler like Slurm to distribute the subprocesses spawned by their pipelines. This can be used to significantly reduce runtime of the slow `CELLRANGER_MULTI` process. This feature is very unstable and can lead to pipelines running indefinetly without failing or processes being killed prematurely. For more information about cluster mode read [this](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-job-submission-mode) and [this](https://www.10xgenomics.com/support/software/cell-ranger/latest/advanced/cr-cluster-mode).

- `--cellranger_disable_ui` - Flag to disable the Web-UI provided by the CellRanger procceses (Safe to use)
- `--cellranger_enable_cluster` - Flag to enable cluster mode
- `--cellranger_cluster_template <path>` - Path to a `.template` file for your respective workload manager - default: `assets/cluster_templates/slurm.template`
- `--cellranger_max_jobs` - Maximum ammount of jobs that can be spawned by a single instance of the CellRanger process - default: 4
- `--cellranger_mem_per_core` - Maximum ammount of Memory consumed per CPU
