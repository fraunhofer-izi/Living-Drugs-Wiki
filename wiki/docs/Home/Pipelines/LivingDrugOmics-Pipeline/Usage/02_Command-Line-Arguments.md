# Command Line Arguments
When launching the pipeline, several options are available to further configure the execution through command-line arguments. These settings can also be defined in the Params-file, which could be used to document the execution more thoroughly. However, if you prefer to keep the `params` file minimal, using command-line arguments is a valid approach.

## Available Arguments
### Quality Control
If desired, it is possible to skip the Quality Control (QC) step (or individual subprocesses) during the pipeline execution. The following options are available for skipping specific QC steps:

- `--skip_fastqc` to skip FastQC

- `--skip_fastq_screen` to skip FastQ Screen

- `--skip_multiqc` to skip MultiQC

- `--skip_qc` to skip all QC steps entirely

### Profiles
Profiles are a powerful tool for customizing how the pipeline is executed. They can be used to adjust the environment, such as utilizing HPC systems or enabling containerization for processes. There are three preconfigured profiles—`singularity`, `slurm`, and `standard`—which can be enabled using the `-profile` flag when launching Nextflow. You can also combine multiple profiles like so: `nextflow run ... -profile <profile1>,<profile2>,<...> ...`.

#### Singularity
If you want the pipeline to use containers for its processes, ensuring consistent and reproducible results, the `singularity` profile is the way to go. Containers are pulled at runtime as needed, and they come prepackaged with all necessary dependencies for each process. Using the `singularity` profile is the recommended method as it provides consistency and avoids version conflicts.

#### Slurm
The `slurm` profile enables the pipeline to use the Slurm workload manager for distributing processes across a cluster environment. The actual distribution of processes is handled by Nextflow. However, note that the default resource values for processes may not be suitable for your environment. Make sure to adjust them in the `nextflow.config` file accordingly

#### Standard
The `standard` profile simply instructs Nextflow to run the pipeline locally, which is the default behavior. It also expects all required binaries to be in `$PATH` so no containers are used. This profile is enabled by default
