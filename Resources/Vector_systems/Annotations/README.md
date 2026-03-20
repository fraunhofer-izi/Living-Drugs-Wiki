# Changes in the annotatiton for lentiviral_vector_idecel.gtf

## Motivation

Loading the sequence file into SnapGene Viewer did not yield any feature annotation for th 3'LTR region. \
The lentiviral_vector_idecel.gtf only has one entry for the 3'LTR region that coincides with the position of the 5'LTR region: \
* line 7: vector	AddedGene	generic_feature	801	981	.	+	.	gene_id "truncHIV-1_3_LTR"; gene_name "truncHIV-1_3_LTR"

We tried to find the correct 3'LTR region. Both LTR regions should flank the CAR construct.

## Approach

Assumption: 5'LTR and 3'LTR regions usually have the same sequence. \
Searching for the corresponding 3'LTR region based on the sequence from the 5'LTR region sourced from the vector sequence. \
The search was done in 50 nt chunks. starting from the first 50 nt of the 5'LTR and extended by another 50 nt.
1) starting from the first 50 nt of the 5'LTR
2) if sequence is found: extended by another 50 nt and repeat extension
3) if sequence is not found: truncate sequence until a match is found == maximum alignment is found

This could be done in a normal text editor or \
more professionaly in the SerialCloner software (version 2.61.) which also returns the position of multimappers via the "Find" function (see image).

Only the first 95 nucleotides of the 5'LTR sequence could be found a second time in the whole vector sequence at position 4736. \
Therefore it is suggested as the putative 3'LTR region.
