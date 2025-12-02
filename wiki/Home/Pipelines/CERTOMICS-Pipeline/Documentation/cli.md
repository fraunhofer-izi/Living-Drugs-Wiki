# Command Line Arguments
When launching the pipeline, several options are available to further configure the execution through command-line arguments. These settings (excluding Nextflow-specific arguments starting with `-` instead of `--`) can also be defined in the [Params-file](./params-file.md), which can be used to document execution more thoroughly. However, if you prefer to keep the params-file minimal, using command-line arguments is a valid approach.

### Profiles
Profiles are a powerful tool for customizing how the pipeline is executed. They can be used to adjust the execution environment, such as utilizing HPC systems or enabling containerization for processes. There are three preconfigured profiles: `singularity`, `slurm` and `standard` which can be enabled using the `-profile` flag when launching Nextflow. You can also combine multiple profiles like so: 

```sh
nextflow run ... -profile <profile1>,<profile2>,<...>
```

You can also define your own profiles by changing the `nextflow.config`. Read the [Nextflow documentation about profiles](https://www.nextflow.io/docs/latest/config.html#config-profiles) if you are interested in doing so.

#### Singularity
To ensure consistent and reproducible results, use the `singularity` profile, which runs pipeline processes in containers. The containers are pulled at runtime as needed, and they come prepackaged with all necessary dependencies for each process. Using the `singularity` profile is the recommended method as it provides consistency and avoids version conflicts.

#### Slurm
The `slurm` profile enables the pipeline to use the Slurm workload manager for distributing processes across a cluster environment. The actual distribution of processes is handled by Nextflow. However, note that the default resource values for processes may not work for your environment. Make sure to adjust them in the `nextflow.config` file accordingly.

#### Standard
The `standard` profile simply instructs Nextflow to run the pipeline locally, which is the default behavior. It also expects all required binaries to be in `$PATH` so no containers are used. This profile is enabled by default.

### Quality Control
If desired, it is possible to skip the Quality Control (QC) steps (or individual subprocesses) during the pipeline execution. The following flags are available for skipping specific QC steps:

- `--skip_fastqc` - Flag to skip FastQC

- `--skip_fastq_screen` - Flag to skip FastQ Screen

- `--skip_multiqc` - Flag to skip MultiQC

- `--skip_qc` - Flag to skip all QC steps entirely
