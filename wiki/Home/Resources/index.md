# Resource on CAR T Cell Therapies

This repository supports the analysis and development of CAR-T cell therapies by providing curated sequence and annotation data for common FDA-approved and non-approved CAR products. For details on data sources (e.g. patents) and the annotation process, see the [Sequence Retrieval and Annotation Process](https://david.schmidt.ribogitpages.izi.fraunhofer.de/living-drugs-wiki/Home/Resources/Methods/) section. It is regularly updated to ensure access to the latest information in this rapidly advancing field.

## CAR Constructs

**CAR constructs** — engineered gene sequences encoding chimeric antigen receptors — can differ significantly across therapies. These variations necessitate tailored approaches for the accurate detection of CAR-positive cells, for example through single-cell sequencing, and can substantially influence the function and behavior of CAR-T cells. **For more information see:** [**CAR constructs**](./CAR-constructs.md). This repository includes detailed nucleotide sequences and annotation data for CAR constructs from the latest publicly available CAR-T therapies.

## Vector Systems

**Vector systems** — such as viral vectors used to deliver CAR constructs into T cells — are critical for determining the efficiency, safety, and stability of gene transfer. Vector systems vary in key components, including promoter type, regulatory elements, and backbone sequences, all of which impact CAR expression and genomic integration. **For more information see:** [**Vector systems**](./Vector-systems.md). To support deeper analysis, the repository also provides full vector sequences and annotations, which are essential for applications like integration site analysis. These data enable researchers to evaluate how CAR constructs integrate into the genome, a crucial factor in assessing the safety and efficacy of CAR-T cell therapies and to compare functional differences between vector systems.

<br>

<figure class="half-size">
  <img src="../../images/resources/Abb_Vecor_Construct.png" alt="Vector and CAR construct">
  <figcaption>Image adapted from <a href="https://bpsbioscience.com/custom-car-t-cell-development">bpsbioscience.com</a></figcaption>
</figure>


## Resources

<div class="grid cards" markdown>

-   __CAR constructs__

    ---

    Get nucleotide sequences `.fasta` and annotation information `.gtf`


    [:dna: Nucleotide sequence](https://github.com/fraunhofer-izi/Living-Drugs-Wiki/tree/main/Resources/CAR_constructs/Sequences)

    [:page_facing_up: Annotations](https://github.com/fraunhofer-izi/Living-Drugs-Wiki/tree/main/Resources/CAR_constructs/Annotations)

-   __Vectors systems__

    ---

    Get nucleotide sequences `.fasta` and annotation information `.gtf`


    [:dna: Nucleotide sequence](https://github.com/fraunhofer-izi/Living-Drugs-Wiki/tree/main/Resources/Vector_systems/Sequences) 

    [:page_facing_up: Annotations](https://github.com/fraunhofer-izi/Living-Drugs-Wiki/tree/main/Resources/Vector_systems/Annotations)

-   __Full documentation__

    ---

    View "Sequence Retrieval and Annotation Process" on how and where sequence and annotation information was retrieved.

    [:material-script-text: Sequence Retrieval and Annotation Process](./Methods.md)

</div>