# Contributing New CAR Constructs

This page provides guidelines for contributing new CAR constructs to the curated resource. 
Community participation is essential to ensure the database remains up to date as new CAR therapeutics are developed. 
All contributions should be submitted via **GitHub pull request**.

---

## Required Files

Each CAR construct must include the following files:

### 1. DNA FASTA File
- Provide the nucleotide sequence in `.fasta` format.
- The sequence must match the original source (e.g., patent, publication, public sequence database).
- The curators will verify the sequence against the cited reference (see README).

### 2. Protein FASTA File
- Provide the amino-acid sequence in `.fasta` format.
- The sequence must be:
  - translated directly from the DNA FASTA file, **or**
  - taken from the original document (if available).
- If taken from a reference, cite the source in the README explicitly.

### 3. GTF Annotation File
- Provide a `.gtf` file annotating the functional domains of the CAR.
- Typical annotated domains include: signal peptide, scFv (VH/VL), hinge, transmembrane domain, co-stimulatory domains, activation domain, tags, and linkers.
- Annotations should follow standard GTF conventions and refer to the protein-level sequence.

### 4. README File
Each CAR submission must include a `README.md` containing:

#### A. Annotation Methodology (GTF)
- Describe how domain boundaries were identified (e.g., based on publications, alignments, domain prediction tools, information from patents).

#### B. Source of the Sequence (FASTA)
- Provide detailed references for the DNA and/or protein sequences:
  - Patent number with page/figure
  - Publication (title, authors, DOI)
  - NCBI accession
- How it could look like:
  https://fraunhofer-izi.github.io/Living-Drugs-Wiki/Home/Resources/Methods/#sources-of-sequences

#### C. Additional Notes (Optional)
- Include relevant information such as isoforms, variants, unusual annotation decisions, or supporting comments.

---

## Submission Workflow

1. **Fork the repository** on GitHub.
2. Create a new folder inside the appropriate directory (one folder per CAR construct).
3. Add the required files:
   - `dna.fasta`
   - `protein.fasta`
   - `annotation.gtf`
   - `README.md`
4. Commit your changes with a descriptive message.
5. Open a **pull request** to the main repository.
   - Include a short summary of the construct and its source.
6. The curatorial team will:
   - Verify the sequence against the cited source
   - Check annotation accuracy
   - Review the README for completeness
   - Request changes if necessary
   - Approve and merge the contribution

---

## Quality Standards

To ensure high-quality and reproducible submissions:

- All sequences must be traceable to the cited sources.
- Annotations must be reproducible based on the README.
- Contributors must verify their translations and domain boundaries.
- Curators will perform an independent quality check before merging.

---

## Contact

For questions or clarification, please open an issue on GitHub or contact us at [christina.kuhn@izi.fraunhofer.de](mailto:christina.kuhn@izi.fraunhofer.de).
