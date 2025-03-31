# Resource on CAR T-Cell Therapies

This repository serves as a **resource** to support the analysis and development of CAR T cell therapies by providing comprehensive sequence and annotation data. For original sources and annotation process see [Methods and Scripts](https://david.schmidt.ribogitpages.izi.fraunhofer.de/living-drugs-wiki/Home/Resources/Methods/).

**CAR constructs** — engineered gene sequences encoding the chimeric antigen receptor — can vary significantly between therapies. These differences require tailored approaches for accurate detection of CAR-positive cells, for example, through single-cell sequencing. :arrow_right: **For a more in-depth explanation about the different CAR constructs see:** [CAR constructs](./CAR-constructs.md)

In addition, **vector systems** — delivery tools such as viral vectors used to introduce CAR constructs into T cells — play a critical role in determining the efficiency, safety, and stability of gene transfer. Used vector systems themselves differ in key features, such as the type of promoter used, regulatory elements, and backbone sequences, all of which can impact CAR expression and genomic integration. :arrow_right: **For a more in-depth explanation about the vector systems, see:**[Vector systems](./Vector-systems.md)

<figure class="half-size">
  <img src="../../images/resources/Abb_Vecor_Construct.png" alt="Vector and CAR construct">
  <figcaption>Image adapted from <a href="https://bpsbioscience.com/custom-car-t-cell-development">bpsbioscience.com</a></figcaption>
</figure>

## Key Features

- **CAR constructs**: Includes detailed nucleotide sequence and annotation data of CAR construct from the latest (public available) CAR T cell therapies. These data is crucial for researchers to understand the specific characteristics and behaviors of different CAR constructs.
- **Vector Systems**: Provides complete vector sequences and annotations, which are critical for applications such as integration site analysis. These data help researchers evaluate how CAR constructs integrate into the genome—an important factor for assessing the safety and efficacy of CAR T cell therapies. 
- **Continuous Updates**: This repository is designed to be continuously updated with new data and resources as they become available, ensuring that users have access to the most current information in the field of CAR T-cell therapy.

## Resources

<div class="grid cards" markdown>

-   __CAR constructs__

    ---

    Get nucleotide sequences `.fasta` and annotation information `.gtf`


    [:dna: Nucleotide sequence](https://github.com/fraunhofer-izi/TODO/-/tree/main/Resources/CAR_constructs/Sequences)

    [:page_facing_up: Annotations](https://github.com/fraunhofer-izi/TODO/-/tree/main/Resources/CAR_constructs/Annotations)

-   __Vectors systems__

    ---

    Get nucleotide sequences `.fasta` and annotation information `.gtf`


    [:dna: Nucleotide sequence](https://github.com/fraunhofer-izi/TODO/-/tree/main/Resources/Vector_systems/Sequences) 

    [:page_facing_up: Annotations](https://github.com/fraunhofer-izi/TODO/-/tree/main/Resources/Vector_systems/Annotations)

-   __Full documentation__

    ---

    View Methods & Scripts on how and where sequence and annotation information was retrieved.

    [:material-script-text: Methods and Scripts](./Methods.md)

</div>