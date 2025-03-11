# CAR Constructs

This page summarizes information on FDA-approved and non-approved chimeric antigen receptors (CAR) constructs. This serves as a comprehensive resource for researchers and bioinformaticians working with CAR T-cell profiling. CAR constructs are divided into different generations referring to the different stages of development, with each generation introducing improvements to enhance efficacy, persistence, and safety. Below, both FDA-approved and non-approved CAR products are presented with detailed descriptions of their structural differences. Precise knowledge of CAR sequences is essential for performing in-depth sequence analyses, including accurate identification of CAR expression, detection of potential mutations, assessment of binding affinities, and evaluation of immunogenicity, all critical for optimizing CAR design and functionality.


<figure class="half-size">
  <img src="/car-flow/uploads/Abb_CAR_generations.png" alt="CAR Generations">
  <figcaption>Image adapted from <a href="doi:10.3390/biomedicines10071493">Moreno, Carlos et al. Biomedicines (2022)</a></figcaption>
</figure>

## Link to Resources

<div class="grid cards" markdown>

-   __CAR constructs__

    ---

    Get nuceleotide sequences `.fasta` and annotation information `.gtf`


    [:dna: Nucleotide sequence](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/tree/main/Resources/CAR_constructs/Sequences)  

    [:page_facing_up: Annotations](https://ribogit.izi.fraunhofer.de/david.schmidt/car-flow/-/tree/main/Resources/CAR_constructs/Annotations)

</div>


## FDA-Approved CAR-T Cell Therapies

<figure>
  <img src="/car-flow/uploads/Abb_FDA_approved.png" alt="FDA-approved">
  <figcaption>Image adapted from <a href="doi:10.3390/biomedicines12081641">Grahnert et al. Biomedicines (2020)</a> *novel CD19 CAR (CAT = using a CAT131E10 hybridoma (CAT)) with a lower affinity than FMC63, which is used in the other approved anti-CD19 CARs</figcaption>
</figure>


### 1. Idecabtagene Vicleucel (Abecma)

- **Indication:** Multiple Myeloma
- **Approval Date:** March 26, 2021
- **Antigen Target:** BCMA (B-cell maturation antigen)
- **CAR Construct Structure:**
    - CD8a signal peptide
    - BCMA scFv (VHH1 linker G4S VHH2)
    - CD8a hinge
    - CD8a transmembrane domain
    - CD137/4-1BB cytoplasmic
    - CD3ζ cytoplasmic

### 2. Ciltacabtagene Autoleucel (Carvykti)

- **Indication:** Multiple Myeloma
- **Approval Date:** February 28, 2022
- **Antigen Target:** BCMA (B-cell maturation antigen)
- **CAR Construct Structure:**
    - CD8a signal peptide
    - BCMA scFv (VHH1 linker G4S VHH2)
    - CD8a hinge
    - CD8a transmembrane domain
    - CD137/4-1BB cytoplasmic
    - CD3ζ cytoplasmic

### 3. Tisagenlecleucel (Kymriah)

- **Indication:** Acute Lymphocytic Leukemia
- **Approval Date:** August 30, 2017
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - CD8 signal peptide
    - FMC63 (anti-CD19)
    - CD8alpha (hinge and TMD)
    - CD137/4-1BB
    - CD3ζ

### 4. Axicabtagene Ciloleucel (Yescarta)

- **Indication:** B-cell Lymphoma
- **Approval Date:** October 18, 2017
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - CSF2RA signal peptide RefSeq
    - FMC63 (anti-CD19)
    - CD28 (part of extracellular, TMD, and intracellular)
    - CD3ζ (complete intracellular domain)

### 5. Brexucabtagene Autoleucel (Tecartus)

- **Indication:** Mantle Cell Lymphoma or Acute Lymphocytic Leukemia
- **Approval Date:** July 24, 2020 (MCL), October 1, 2021 (ALL)
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - anti-CD19 (FMC63)
    - CD28 (part of extracellular, TMD, and intracellular part)
    - CD3ζ

### 6. Lisocabtagene Maraleucel (Breyanzi)

- **Indication:** B-cell Lymphoma
- **Approval Date:** February 5, 2021
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - anti-CD19 (FMC63)
    - IgG4 (hinge)
    - CD28 (TMD)
    - CD137/4-1BB
    - CD3ζ

### 7. Obecabtagene Autoleucel (Aucatzyl; Autolus Inc)

- **Indication:** Relapsed or refractory (R/R) B-cell precursor acute lymphoblastic leukemia (ALL)
- **Approval Date:** November 8, 2024 [Link](https://www.cgtlive.com/view/fda-approves-obe-cel-adults-relapsed-refractory-b-cell-precursor-acute-lymphoblastic-leukemia)
- **Antigen Target:** CD19
- **CAR Construct Structure:** To be updated.

## Non-FDA Approved CAR-T and Related Therapies

### 1. APRIL-based CAR (Third-Generation)

- **Status:** Not yet FDA approved (Wang et al., 2021)
- **Antigen Target:** Dual-antigen CAR: BCMA and TACI (Cyclophilin Ligand Interactor)
- **Indication:** Multiple Myeloma
- **CAR Construct Structure:**
    - **Patent:** No17 (Patent April)
    - **Protein Region:** 116-250 of APRIL protein (Uniprot 075888)
    - **Signal Peptide:** IgK k chain V-III
    - **Scaffold:** CAR scaffold comprising IgG1 hinge spacer, CD8 alpha spacer, or IgG1 Fc domain

### 2. ROR1 CAR 

- **Status:** Study by Osorio-Rodriguez (2023)
- **Antigen Target:** ROR1
- **Indication:** Leukemia, lymphoma, and some solid tumors overexpress ROR1
- **CAR Construct Structure:**
    - **ScFv:** R11 or R12-scFv (mouse cells do not carry R12)
    - **Hinge:** IG4-hinge
    - **Costimulatory Domains:** CD28, 4-1BB
    - **Signaling Domain:** CD3ζ
    - **Additional Components:** T2A viral protein (ribosomal skipping), truncated EGFR (safety switch to detect CAR+ expressing cells with anti-EGFR antibody)

### 3. Mesothelin-Directed CAR

- **Status:** [NCT03054298](https://clinicaltrials.gov/study/NCT03054298)
- **Antigen Target:** Simultaneously binds myeloma cells expressing BCMA and T cells (via CD3)
- **Indication:** Relapsed/Refractory Multiple Myeloma (RRMM)
- **Drug:** Alnuctamab (Bi-specific T Cell Engager)
- **References:**
    - [ASH Publications](https://ashpublications.org/blood/article/140/Supplement%201/400/491672/Alnuctamab-ALNUC-BMS-986349-CC-93269-a-B-Cell)
    - [Cell Cancer](https://www.cell.com/cancer-cell/fulltext/S1535-6108(17)30016-8#secsectitle0080)

### 4. GPRC5D-Targeted CAR T-Cell

- **Status:** Early-stage clinical trials
- **Antigen Target:** GPRC5D
- **Indication:** Multiple Myeloma (Relapsed/Refractory)
- **Clinical Trial:** [BMS-986393/CC-95266](https://ashpublications.org/blood/article/142/Supplement%201/219/499690/BMS-986393-CC-95266-a-G-Protein-Coupled-Receptor)
- **References:**
    - [ASH Publications](https://ashpublications.org/thehematologist/article/doi/10.1182/hem.V20.1.202314/494129/GPRC5D-The-Next-Frontier-for-Immunotherapy-in)


### 5. KYV-101 (Kyverna Therapeutics)

- **Status:** Early clinical trials
- **Antigen Target:** CD19
- **Indication:** KYV-101 was developed by Kyverna Therapeutics for the treatment of B cell-driven autoimmune diseases, such as lupus nephritis, systemic sclerosis, myasthenia gravis, and stiff-person syndrome
- **CAR Construct Structure:**
    - Construct C19 binding domain (Hu19)
    - CD8a hinge and transmembrane domain
    - CD28 co-stimulatory domain
    - CD3ζ activation domain

### Allogenic CAR T cells 

#### 1. CD19 directed ALLO-501 (Allogene Therapeutics)

- **Status:** Phase 2
- **Indication:** Non-Hodgkin Lymphoma
- **Mechanism:** An allogeneic CAR-T therapy aiming to provide a safer and more accessible off-the-shelf option.

#### 2. FT819 (Fate Therapeutics)

- **Status:** Phase 1
- **Indication:** Relapsed/Refractory B-Cell Malignancies
- **Antigen Target:** CD19
- **Mechanism:** An off-the-shelf, allogeneic CAR-T therapy currently being studied for safety and dosing, with potential progression to phase 2.

#### 3. BCMA and CD19 dual CAR T therapy: GC012F (Gracell Biotechnologies)

- **Status:** Phase 1/2
- **Indication:** Multiple Myeloma
- **Mechanism:** A dual-target CAR-T therapy currently in the transition between phases 1 and 2, as safety data support further trials.

#### 4. P-BCMA-101 (Poseida Therapeutics)

- **Status:** Phase 2
- **Antigen Target:** BCMA
- **Indication:** Multiple Myeloma
- **Mechanism:** P-BCMA-101 is a novel chimeric antigen receptor (CAR)-T cell therapeutic targeting BCMA, which is highly expressed on multiple myeloma cells. It is designed to increase efficacy while minimizing toxicity through reduced immunogenicity, lack of tonic signaling, a safety switch, and a product composed predominantly of early memory T cells that are effectively all CAR-positive.

#### 5. ATA2271 (Atara Biotherapeutics)

- **Status:** Phase 1
- **Antigen Target:** Mesothelin
- **Indication:** Solid Tumors
- **Mechanism:** ATA2271 is a mesothelin-targeting CAR-T therapy for solid tumors, currently in phase 1 trials to establish safety and initial efficacy.
