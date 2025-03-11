from Bio import SeqIO
from Bio.Seq import Seq

def find_nucleotide_substring(nucleotide_file, protein_file, search_pattern_protein):
    """
    Find the nucleotide sequence substring corresponding to a given protein pattern.

    Args:
        nucleotide_file (str): Path to the nucleotide FASTA file.
        protein_file (str): Path to the protein FASTA file.
        search_pattern_protein (str): Protein sequence pattern to search for.

    Returns:
        str: The corresponding nucleotide sequence substring, or a message if not found.
    """
    # Read nucleotide and protein sequences
    nucleotide_record = next(SeqIO.parse(nucleotide_file, "fasta"))
    protein_record = next(SeqIO.parse(protein_file, "fasta"))

    nucleotide_seq = nucleotide_record.seq
    protein_seq = protein_record.seq

    # Search for the protein pattern in the protein sequence
    protein_index = str(protein_seq).find(search_pattern_protein)
    if protein_index == -1:
        return f"Protein pattern '{search_pattern_protein}' not found in protein sequence."

    # Convert protein index to nucleotide indices
    nucleotide_start = protein_index * 3
    nucleotide_end = nucleotide_start + len(search_pattern_protein) * 3

    # Extract the corresponding nucleotide substring
    nucleotide_substring = nucleotide_seq[nucleotide_start:nucleotide_end]
    return str(nucleotide_substring)


# Example usage
if __name__ == "__main__":
    nucleotide_file = "/homes/olymp/christina.kuhn/christina.kuhn/work/car-flow/Resources/CAR_constructs/Sequences/Hu19-CD28Z_MN698642.1.fasta"
    protein_file = "/homes/olymp/christina.kuhn/christina.kuhn/work/car-flow/Resources/CAR_constructs/Sequences/Hu19-CD28Z_MN698642.1_protein.fasta"
    search_pattern_protein = "MALPVTALLLPLALLLHAARP"

    result = find_nucleotide_substring(nucleotide_file, protein_file, search_pattern_protein)
    print(f"Result: {result}")
