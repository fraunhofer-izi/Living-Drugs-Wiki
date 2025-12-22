# Extending the pipeline

If your use case needs additional processes that are not covered in the current implementation that you would like to be executed alongside the other processes, then you have the option to extend the existing workflows with your own. To do that, you need to clone the pipeline repository found on GitHub and locate the source files defining the process behavior. 

## Adding a custom process

### Where to find your process Input

If you just need to add a process to the pipeline to include a tool you rely on, you need to first identify the inputs that your tool needs. Your inputs could be anything between simple integer values and files produced by other processes. Once you know what inputs you need, you can start to think about where you want to actually place the process. The pipeline behavior is defined in multiple Nextflow files, each defining a workflow with its own inputs and outputs. To avoid having to change any of these workflow inputs or outputs, it makes sense to place your process in a script with a workflow that already has all the variables you need. To help you find the ideal script to use, we compiled a list with the most important variables available in the workflows defined in each script. If your dependencies are not available in a single workflow, you are going to have to change the outputs  emitted and inputs received by the workflow containing the variables you are interested in as well as applying those changes in the primary workflow defined in `main.nf`.

#### `handle_references.nf`

|Source|Variable name|Description|
|-|-|-|
|Workflow input|`carFasta`, `carGtf`|CAR-Construct files|
|Process: `BUILD_REFERENCE`|`BUILD_REFERENCE.out`|Custom gene expression reference|

#### `quality_control.nf`

|Source|Variable name|Description|
|-|-|-|
|Workflow input|`samples`|Input samples provided by the samplesheet|
|Workflow input|`cellrangerReports`|Web-summary reports produced by the `CELLRANGER_MULTI` process|
|Process: `FASTQC`|`FASTQC.out`|FastQC reports|
|Process: `FASTQ_SCREEN`|`FASTQ_SCREEN.out`|FastQ_Screen reports|
|Process: `MULTIQC`|`MULTIQC.out`|MultiQC report|

#### `secondary_analysis.nf`

|Source|Variable name|Description|
|-|-|-|
|Workflow input|`samples`|Input samples provided by the samplesheet|
|Workflow input|`gexReference`, `vdjReference`, `featureReference`|References used by the `CELLRANGER_MULTI` process|
|Workflow input|`carFasta`, `carGtf`|CAR-Construct files|
|Process: `CELLRANGER_MULTI`|`CELLRANGER_MULTI.out.*`|Multiple relevant outputs produced by the `CELLRANGER_MULTI` process for each sample|
|Process: `SEURAT_OBJECT`|`SEURAT_OBJECT.out`|Seurat object built based on the `CELLRANGER_MULTI` output|
|Process: `CAR_METRICS`|`CAR_METRICS.out.*`|Multiple relevant outputs produced by the `CAR_METRICS` process|

### Adding a new process to a workflow

Once you find a workflow with all the data you need, you can integrate it into the workflow definition. To help with an example, we are going to add a new process that takes the websummary output produced by the `CELLRANGER_MULTI` process of each sample and modifies it in some way. For this example, it would be reasonable to place the process definition in the `workflows/secondary_analysis.nf` script. Here you can directly access the process output like this:

```nextflow
workflow SECONDARY_ANALYSIS {
    take:
    ...

    main:
    ...

    CELLRANGER_MULTI(...)
    CUSTOM_PROCESS( CELLRANGER_MULTI.out.webSummary )
    
    ...
}
```

The process definition itself is relatively straight forward:

```nextflow
process CUSTOM_PROCESS {
    // your directives

    input:
    path webSummary

    output:
    path 'modified_web_summary.html'

    script:
    """
    # add your code here
    """
}
```

Because the definition of a process is best explained by the Nextflow documentation, you are best advised to look [here](https://www.nextflow.io/docs/latest/process.html) if you need help with the basic syntax.

### Common directives

Important directives you might find used in other processes are the `label`, `publishDir` and `fair` directives. The `label` directive is usually used in order to move process configuration into the `nextflow.config` file. Most of the time they are used to define the containers used to run the processes in. If you want your process to be run in a containerized environment, you can define a custom label in the `nextflow.config`. Under the `singularity` section, you can add a new label by adding an entry to the `process` subsection like this:

```
singularity {
    singularity.enabled = true
    singularity.autoMounts = true
    
    process {
        withLabel: module_cellranger { ... }
        
        withLabel: module_customprocess {
            container = "/your/container.sif"
        }
    }
}
```

You can then use the `label` directive in your own process definition to use that container when the pipeline is running using the `singularity` profile. The `publishDir` directive can be used to move the output produced by your process to a predefined directory once the process is done. This is very useful when you want to use the process output without having to search through the working directories. Another directive commonly used in combination with the `publishDir` directive is `tag` the directive. If your process is supposed to run multiple times (for example, once for each sample), you can use the `tag` directive to identify each instance by a name. If you use this in combination with the `publishDir` directive, each instance will get its own subdirectory in the defined location to avoid collisions. You can find more information about directives and how to use them in the [official documentation](https://www.nextflow.io/docs/latest/process.html#directives).
