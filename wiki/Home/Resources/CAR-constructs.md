# CAR Constructs

This page summarizes information on FDA-approved and non-approved chimeric antigen receptors (CAR) constructs. This serves as a comprehensive resource for researchers and bioinformaticians working with CAR T-cell profiling. 


CAR constructs are categorized into different generations, each representing a stage of development. With each generation, specific enhancements are introduced—such as the addition of co-stimulatory domains (e.g., CD28, 4-1BB), improvements in antigen-binding affinity, signaling strength, or persistence, and the incorporation of safety switches or logic gating. These modifications are designed to increase therapeutic efficacy, prolong cell survival, and reduce toxicity or off-target effects.

Below, both FDA-approved and non-approved CAR products are presented with detailed descriptions of their structural differences regarding the CAR construct. Precise knowledge of CAR sequences is essential for performing in-depth sequence analyses, including accurate identification of CAR expression, detection of potential mutations, assessment of binding affinities, and evaluation of immunogenicity, all critical for optimizing CAR design and functionality.


<figure class="half-size">
  <img src="../../../images/resources/Abb_CAR_generations.png" alt="CAR generations">
  <figcaption>Image adapted from <a href="https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.1034707/full"> Tomasik et. al 2022 </a></figcaption>
</figure>

## Link to Resources

<div class="grid cards" markdown>

-   __CAR constructs__

    ---

    Get nuceleotide sequences `.fasta` and annotation information `.gtf`

    [:dna: Nucleotide sequence](https://github.com/fraunhofer-izi/Living-Drugs-Wiki/tree/main/Resources/CAR_constructs/Sequences)

    [:page_facing_up: Annotations](https://github.com/fraunhofer-izi/Living-Drugs-Wiki/tree/main/Resources/CAR_constructs/Annotations)
</div>


## FDA-Approved CAR T Cell Therapies

<figure>
  <img src="../../../images/resources/Abb_FDA_approved.png" alt="FDA-approved">
  <figcaption>Image adapted from <a href="doi:10.3390/biomedicines12081641">Grahnert et al. Biomedicines (2020)</a> *novel CD19 CAR (CAT = using a CAT131E10 hybridoma (CAT))</figcaption>
</figure>


### FDA-Approved CAR T Cell Therapies – Summary Table

| Therapy Name | Approval Date | Antigen Target | Indication | Antigen Recognition | Spacer | Transmembrane | Signaling | Link |
|--------------|----------------|----------------|------------|----------------------|--------|----------------|-----------|------|
| [Idecabtagene Vicleucel (Abecma)](https://www.drugs.com/pro/abecma.html) | 2021-03-26 | BCMA | Multiple Myeloma | BCMA scFv (VHH1-G4S-VHH2) | CD8a hinge | CD8a transmembrane domain | 4-1BB, CD3ζ | https://www.drugs.com/pro/abecma.html |
| [Ciltacabtagene Autoleucel (Carvykti)](https://www.drugs.com/pro/carvykti.html) | 2022-02-28 | BCMA | Multiple Myeloma | BCMA scFv (VHH1-G4S-VHH2) | CD8a hinge | CD8a transmembrane domain | 4-1BB, CD3ζ | https://www.drugs.com/pro/carvykti.html |
| [Tisagenlecleucel (Kymriah)](https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/kymriah-tisagenlecleucel) | 2017-08-30 | CD19 | Acute Lymphocytic Leukemia | FMC63 (anti-CD19) | CD8 hinge | CD8 TMD | 4-1BB, CD3ζ | https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/kymriah-tisagenlecleucel |
| [Axicabtagene Ciloleucel (Yescarta)](https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/yescarta-axicabtagene-ciloleucel) | 2017-10-18 | CD19 | B-cell Lymphoma | FMC63 (anti-CD19) | CD28 extracellular | CD28 TMD | CD28 intracellular, CD3ζ | https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/yescarta-axicabtagene-ciloleucel |
| [Brexucabtagene Autoleucel (Tecartus)](https://www.drugs.com/pro/tecartus.html) | 2020-07-24 | CD19 | MCL / ALL | FMC63 (anti-CD19) | CD28 extracellular | CD28 TMD | CD28 intracellular, CD3ζ | https://www.drugs.com/pro/tecartus.html |
| [Lisocabtagene Maraleucel (Breyanzi)](https://www.drugs.com/pro/breyanzi.html) | 2021-02-05 | CD19 | B-cell Lymphoma | FMC63 (anti-CD19) | IgG4 hinge | CD28 TMD | 4-1BB, CD3ζ | https://www.drugs.com/pro/breyanzi.html |
| [Obecabtagene Autoleucel (Obe-cel / Aucatzyl)](https://www.cgtlive.com/view/fda-approves-obe-cel-adults-relapsed-refractory-b-cell-precursor-acute-lymphoblastic-leukemia) | 2024-11-08 | CD19 | R/R B-cell precursor ALL | CAT131E10 (anti-CD19, low affinity) | CD8a hinge | CD8a TMD | 4-1BB, CD3ζ | https://www.cgtlive.com/view/fda-approves-obe-cel-adults-relapsed-refractory-b-cell-precursor-acute-lymphoblastic-leukemia |


### 1. [**Idecabtagene Vicleucel (Abecma)**](https://www.drugs.com/pro/abecma.html)  

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

### 2. [**Ciltacabtagene Autoleucel (Carvykti)**](https://www.drugs.com/pro/carvykti.html) 

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

### 3. [**Tisagenlecleucel (Kymriah)**](https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/kymriah-tisagenlecleucel)

- **Indication:** Acute Lymphocytic Leukemia
- **Approval Date:** August 30, 2017
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - CD8 signal peptide
    - FMC63 (anti-CD19)
    - CD8alpha (hinge and TMD)
    - CD137/4-1BB
    - CD3ζ

### 4. [**Axicabtagene Ciloleucel (Yescarta)**](https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/yescarta-axicabtagene-ciloleucel)  

- **Indication:** B-cell Lymphoma
- **Approval Date:** October 18, 2017
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - CSF2RA signal peptide RefSeq
    - FMC63 (anti-CD19)
    - CD28 (part of extracellular, TMD, and intracellular)
    - CD3ζ (complete intracellular domain)

### 5. [**Brexucabtagene Autoleucel (Tecartus)** ](https://www.drugs.com/pro/tecartus.html)  

- **Indication:** Mantle Cell Lymphoma or Acute Lymphocytic Leukemia
- **Approval Date:** July 24, 2020 (MCL), October 1, 2021 (ALL)
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - anti-CD19 (FMC63)
    - CD28 (part of extracellular, TMD, and intracellular part)
    - CD3ζ

### 6. [**Lisocabtagene Maraleucel (Breyanzi)**](https://www.drugs.com/pro/breyanzi.html)  

- **Indication:** B-cell Lymphoma
- **Approval Date:** February 5, 2021
- **Antigen Target:** CD19
- **CAR Construct Structure:**
    - anti-CD19 (FMC63)
    - IgG4 (hinge)
    - CD28 (TMD)
    - CD137/4-1BB
    - CD3ζ

### 7. [**Obecabtagene Autoleucel (Obe-cel / Aucatzyl)**](https://www.cgtlive.com/view/fda-approves-obe-cel-adults-relapsed-refractory-b-cell-precursor-acute-lymphoblastic-leukemia)  

- **Indication:** Relapsed or refractory (R/R) B-cell precursor acute lymphoblastic leukemia (ALL)
- **Approval Date:** November 8, 2024 [Link](https://www.cgtlive.com/view/fda-approves-obe-cel-adults-relapsed-refractory-b-cell-precursor-acute-lymphoblastic-leukemia)
- **Antigen Target:** CD19
- **CAR Construct Structure:** 
    - anti-CD19 (novel CD19 CAR (CAT = using a CAT131E10 hybridoma (CAT)) with a lower affinity than FMC63)
    - CD8a (hinge and TMD)
    - CD137/4-1BB
    - CD3ζ

## Non-FDA Approved CAR T and Related Therapies

### Non-FDA-Approved CAR T Cell Therapies - Summary Table

| Therapy Name | CAR Design | Antigen Target | Indication | CAR Construct Structure | Link |
|--------------|------------|----------------|------------|--------------------------|------|
| [ALLO-501](https://www.allogene.com/pipeline/allo-501) | Allogeneic | CD19 | Non-Hodgkin Lymphoma | Allogeneic CAR; CD19-specific | https://www.allogene.com/pipeline/allo-501 |
| [FT819](https://fatetherapeutics.com/pipeline/ft819/) | Allogeneic | CD19 | Relapsed/Refractory B-Cell Malignancies | Off-the-shelf iPSC-derived CD19 CAR T | https://fatetherapeutics.com/pipeline/ft819/ |
| [Mesothelin CAR (Alnuctamab)](https://clinicaltrials.gov/study/NCT03054298) | Bi-specific engager | BCMA and CD3 | Relapsed/Refractory Multiple Myeloma | BiTE targeting BCMA on myeloma and CD3 on T cells | https://clinicaltrials.gov/study/NCT03054298 |
| [KYV-101](https://www.kyvernatx.com/pipeline/kyv-101) | Conventional CD19 CAR | CD19 | Autoimmune diseases (e.g., lupus nephritis) | Hu19 scFv, CD8a hinge/TMD, CD28, CD3ζ | https://www.kyvernatx.com/pipeline/kyv-101 |
| [ATA2271](https://www.atarabio.com/pipeline/ata2271/) | Conventional single target | Mesothelin | Solid Tumors | Mesothelin-targeted CAR T | https://www.atarabio.com/pipeline/ata2271/ |
| [GPRC5D CAR](https://ashpublications.org/blood/article/142/Supplement%201/219/499690/BMS-986393-CC-95266-a-G-Protein-Coupled-Receptor) | Conventional single target | GPRC5D | Relapsed/Refractory Multiple Myeloma | GPRC5D-targeted CAR in early clinical development | https://ashpublications.org/blood/article/142/Supplement%201/219/499690/BMS-986393-CC-95266-a-G-Protein-Coupled-Receptor |
| [APRIL-based CAR](https://jitc.bmj.com/content/11/6/e006699) | Dual-targeting | BCMA and TACI | Multiple Myeloma | APRIL protein domain 116–250; IgG1/CD8 spacers | https://jitc.bmj.com/content/11/6/e006699 |
| [GC012F](https://www.gracellbio.com/pipeline/gc012f) | Dual-targeting | BCMA and CD19 | Multiple Myeloma | Dual-target CAR T, phase 1/2 | https://www.gracellbio.com/pipeline/gc012f |
| [P-BCMA-101](https://poseida.com/pipeline/p-bcma-101/) | Safety switch | BCMA | Multiple Myeloma | BCMA CAR with safety switch, memory T cells | https://poseida.com/pipeline/p-bcma-101/ |
| [ROR1 CAR](https://aacrjournals.org/clincancerres/article/31/3/503/751210/Phase-I-Study-of-ROR1-Specific-CAR-T-Cells-in) | Safety switch | ROR1 | Leukemia, lymphoma, solid tumors | R11/R12 scFv, CD28, 4-1BB, CD3ζ, EGFR safety switch | https://aacrjournals.org/clincancerres/article/31/3/503/751210/Phase-I-Study-of-ROR1-Specific-CAR-T-Cells-in |


### 1. [**APRIL-based CAR T Cell Therapy** – JITC (2023)](https://jitc.bmj.com/content/11/6/e006699)  

- **Status:** Not yet FDA approved (Wang et al., 2021)
- **Antigen Target:** Dual-antigen CAR: BCMA and TACI (Cyclophilin Ligand Interactor)
- **Indication:** Multiple Myeloma
- **CAR Construct Structure:**
    - **Patent:** No17 (Patent April)
    - **Protein Region:** 116-250 of APRIL protein (Uniprot 075888)
    - **Signal Peptide:** IgK k chain V-III
    - **Scaffold:** CAR scaffold comprising IgG1 hinge spacer, CD8 alpha spacer, or IgG1 Fc domain

### 2. [**ROR1 CAR T Cell Therapy** – Clinical Cancer Research (2024)](https://aacrjournals.org/clincancerres/article/31/3/503/751210/Phase-I-Study-of-ROR1-Specific-CAR-T-Cells-in) 

- **Status:** Study by Osorio-Rodriguez (2023)
- **Antigen Target:** ROR1
- **Indication:** Leukemia, lymphoma, and some solid tumors overexpress ROR1
- **CAR Construct Structure:**
    - **ScFv:** R11 or R12-scFv (mouse cells do not carry R12)
    - **Hinge:** IG4-hinge
    - **Costimulatory Domains:** CD28, 4-1BB
    - **Signaling Domain:** CD3ζ
    - **Additional Components:** T2A viral protein (ribosomal skipping), truncated EGFR (safety switch to detect CAR+ expressing cells with anti-EGFR antibody)

### 3. [**Mesothelin-Directed CAR T Therapy (NCT03054298)** – ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT03054298)  

- **Status:** [NCT03054298](https://clinicaltrials.gov/study/NCT03054298)
- **Antigen Target:** Simultaneously binds myeloma cells expressing BCMA and T cells (via CD3)
- **Indication:** Relapsed/Refractory Multiple Myeloma (RRMM)
- **Drug:** Alnuctamab (Bi-specific T Cell Engager)
- **References:**
    - [ASH Publications](https://ashpublications.org/blood/article/140/Supplement%201/400/491672/Alnuctamab-ALNUC-BMS-986349-CC-93269-a-B-Cell)
    - [Cell Cancer](https://www.cell.com/cancer-cell/fulltext/S1535-6108(17)30016-8#secsectitle0080)

### 4. [**GPRC5D CAR T (BMS-986393 / CC-95266)** – ASH Publications](https://ashpublications.org/blood/article/142/Supplement%201/219/499690/BMS-986393-CC-95266-a-G-Protein-Coupled-Receptor)  

- **Status:** Early-stage clinical trials
- **Antigen Target:** GPRC5D
- **Indication:** Multiple Myeloma (Relapsed/Refractory)
- **Clinical Trial:** [BMS-986393/CC-95266](https://ashpublications.org/blood/article/142/Supplement%201/219/499690/BMS-986393-CC-95266-a-G-Protein-Coupled-Receptor)
- **References:**
    - [ASH Publications](https://ashpublications.org/thehematologist/article/doi/10.1182/hem.V20.1.202314/494129/GPRC5D-The-Next-Frontier-for-Immunotherapy-in)


### 5. [**KYV-101 (Kyverna Therapeutics)** – Company Website](https://www.kyvernatx.com/pipeline/kyv-101)  

- **Status:** Early clinical trials
- **Antigen Target:** CD19
- **Indication:** KYV-101 was developed by Kyverna Therapeutics for the treatment of B cell-driven autoimmune diseases, such as lupus nephritis, systemic sclerosis, myasthenia gravis, and stiff-person syndrome
- **CAR Construct Structure:**
    - Construct C19 binding domain (Hu19)
    - CD8a hinge and transmembrane domain
    - CD28 co-stimulatory domain
    - CD3ζ activation domain

#### 6. [**GC012F (Gracell Biotechnologies)** – Gracell Pipeline](https://www.gracellbio.com/pipeline/gc012f)  

- **Status:** Phase 1/2
- **Indication:** Multiple Myeloma
- **Mechanism:** A dual-target CAR T cell therapy currently in the transition between phases 1 and 2, as safety data support further trials.

#### 7. [**P-BCMA-101 (Poseida Therapeutics)** – Company Website](https://poseida.com/pipeline/p-bcma-101/)  

- **Status:** Phase 2
- **Antigen Target:** BCMA
- **Indication:** Multiple Myeloma
- **Mechanism:** P-BCMA-101 is a novel chimeric antigen receptor (CAR)-T cell therapeutic targeting BCMA, which is highly expressed on multiple myeloma cells. It is designed to increase efficacy while minimizing toxicity through reduced immunogenicity, lack of tonic signaling, a safety switch, and a product composed predominantly of early memory T cells that are effectively all CAR-positive.

#### 8. [**ATA2271 (Atara Biotherapeutics)** – Company Pipeline](https://www.atarabio.com/pipeline/ata2271/)  

- **Status:** Phase 1
- **Antigen Target:** Mesothelin
- **Indication:** Solid Tumors
- **Mechanism:** ATA2271 is a mesothelin-targeting CAR T cell therapy for solid tumors, currently in phase 1 trials to establish safety and initial efficacy.

### Allogenic CAR T cells 

#### 1. [**ALLO-501 (Allogene Therapeutics)** – Company Pipeline](https://www.allogene.com/pipeline/allo-501)  

- **Status:** Phase 2
- **Indication:** Non-Hodgkin Lymphoma
- **Mechanism:** An allogeneic CAR T cell therapy aiming to provide a safer and more accessible off-the-shelf option.

#### 2.  [**FT819 (Fate Therapeutics)** – Company Pipeline](https://fatetherapeutics.com/pipeline/ft819/)  

- **Status:** Phase 1
- **Indication:** Relapsed/Refractory B-Cell Malignancies
- **Antigen Target:** CD19
- **Mechanism:** Off-the-shelf iPSC-derived CAR T therapy. 
