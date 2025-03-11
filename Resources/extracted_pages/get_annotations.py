from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Entrez

import os
import subprocess
import pandas as pd
import re
import argparse
import json5

def fetch_fasta_from_ncbi(gene_ids, output_file):
    """
    Fetch FASTA sequences from NCBI for a list of gene IDs.

    Args:
        gene_ids (list): List of gene IDs to fetch.
        output_file (str): Path to save the fetched FASTA sequences.

    Returns:
        None
    """
    Entrez.email = "christina.k.kuhn@example.com"  # Replace with your email
    with open(output_file, "w") as fasta_file:
        for gene_id in gene_ids:
            handle = Entrez.efetch(db="nucleotide", id=gene_id, rettype="fasta", retmode="text")
            fasta_data = handle.read()
            handle.close()
            fasta_file.write(fasta_data)


def fetch_gene_names(gene_ids):
    """
    Fetch gene names corresponding to the given gene IDs from NCBI.

    Args:
        gene_ids (list): List of gene IDs to fetch gene names for.

    Returns:
        dict: A dictionary mapping gene IDs to gene names.
    """
    Entrez.email = "christina.k.kuhn@example.com"  # Replace with your email
    gene_name_mapping = {}
    for gene_id in gene_ids:
        handle = Entrez.efetch(db="nucleotide", id=gene_id, rettype="gb", retmode="text")
        record = handle.read()
        handle.close()

        # Extract gene name from the record
        gene_name = None
        for line in record.split("\n"):
            if "gene=" in line:
                gene_name = line.strip().split("gene=")[-1].replace('"', '').replace("'", "")
                break

        gene_name_mapping[gene_id] = gene_name if gene_name else "Unknown"

    return gene_name_mapping


def dna_to_domain_blast(dna_sequence, domain_dna_file, output_blast_file, gtf_output_file, gene_name_mapping, temp_query_file="query_temp.fasta"):
    """
    Compares a DNA sequence with the DNA sequence of protein domains, performs BLAST, and annotates the DNA in GTF format.

    Args:
        dna_sequence (str): DNA sequence as a string.
        domain_dna_file (str): Path to the input DNA file containing protein domain sequences in FASTA format.
        output_blast_file (str): Path to the output BLAST results file.
        gtf_output_file (str): Path to the output GTF annotation file.
        gene_name_mapping (dict): Mapping of gene IDs to gene names.
        temp_query_file (str): Path to a temporary file to store the query sequence for BLAST.

    Returns:
        None
    """
    with open(temp_query_file, "w") as temp_file:
        temp_file.write(f">query\n{dna_sequence}\n")

    db_name = "domain_dna_db"
    makeblastdb_command = f"makeblastdb -in {domain_dna_file} -dbtype nucl -out {db_name}"
    subprocess.run(makeblastdb_command, shell=True, check=True)

    blastn_command = f"blastn -query {temp_query_file} -db {db_name} -outfmt 6 -out {output_blast_file}"
    subprocess.run(blastn_command, shell=True, check=True)

    parse_blast_to_gtf(output_blast_file, gtf_output_file, "query", gene_name_mapping)
    os.remove(temp_query_file)


def parse_blast_to_gtf(blast_results_file, gtf_output_file, gene_id, gene_name_mapping):
    """
    Parse BLAST results and create a sorted GTF annotation file.

    Args:
        blast_results_file (str): Path to the BLAST results file.
        gtf_output_file (str): Path to the output GTF file.
        gene_id (str): Gene ID derived from the DNA sequence file name.
        gene_name_mapping (dict): Mapping of gene IDs to gene names.

    Returns:
        None
    """
    gtf_entries = []
    exon_number = 0

    with open(blast_results_file, 'r') as blast_file:
        for line in blast_file:
            exon_number += 1
            columns = line.strip().split("\t")
            q_start, q_end = int(columns[6]), int(columns[7])
            print(columns)
            exon_id = gene_name_mapping.get(columns[1], "Unknown")

            gtf_entries.append({
                "start": q_start,
                "end": q_end,
                "line": (
                    f"{gene_id}\tAddedGene\texon\t{q_start}\t{q_end}\t.\t+\t.\t"
                    f"gene_id \"{gene_id}\"; transcript_id \"{gene_id}\"; gene_name \"{gene_id}\"; "
                    f"gene_type \"protein_coding\"; transcript_type \"protein_coding\"; "
                    f"exon_number {exon_number}; exon_id \"{exon_id}\";\n"
                ),
            })

    gtf_entries.sort(key=lambda x: (x["start"], x["end"]))

    with open(gtf_output_file, 'w') as gtf_file:
        for entry in gtf_entries:
            gtf_file.write(entry["line"])


def find_flexible_substring_positions(dna_sequence, search_dict):
    """
    Searches for flexible substrings in a DNA sequence string where substrings start with one string
    and end with another string, allowing any sequence in between.

    Args:
        dna_sequence (str): DNA sequence as a string.
        search_dict (dict): A dictionary where the key is the name and the value is a list of
                            [string_start, string_end] to search for as a substring.

    Returns:
        list: A list of dictionaries with the name, start position, end position, and the matched substring.
    """
    results = []
    for name, substrings in search_dict.items():
        if len(substrings) != 2:
            raise ValueError(f"Each value in the dictionary must be a list with two elements. Found: {substrings}")
        string_start, string_end = substrings

        pattern = re.compile(f"{re.escape(string_start)}.*?{re.escape(string_end)}")
        for match in pattern.finditer(dna_sequence):
            start_pos = match.start() + 1
            end_pos = match.end()
            results.append({
                "name": name,
                "start": start_pos,
                "end": end_pos,
                "substring": match.group()[:10]
            })

    return results

def compare_annotations(old_annotation_file, new_annotation_file):
    """
    Compare the old annotation file with the new annotation file.
    
    Args:
        old_annotation_file (str): Path to the old annotation file.
        new_annotation_file (str): Path to the new annotation file.

    Returns:
        pd.DataFrame: DataFrame with differences between old and new annotations.
    """
    def parse_annotation(file_path):
        """
        Parse a GTF file and return a DataFrame.

        Args:
            file_path (str): Path to the GTF file.

        Returns:
            pd.DataFrame: DataFrame with parsed annotation data.
        """
        data = []
        with open(file_path, "r") as file:
            for line in file:
                if not line.startswith("#") and "exon" in line:
                    columns = line.strip().split("\t")
                    start, end = int(columns[3]), int(columns[4])
                    attributes = columns[8]
                    exon_id = None
                    for attr in attributes.split(";"):
                        if "exon_id" in attr:
                            exon_id = attr.split("\"")[1]
                    data.append({"start": start, "end": end, "exon_id": exon_id})
        return pd.DataFrame(data)

    # Parse both old and new annotations
    old_df = parse_annotation(old_annotation_file)
    new_df = parse_annotation(new_annotation_file)

    # Merge to find matches and differences
    comparison = pd.merge(
        old_df, new_df, on=["start", "end"], how="outer", suffixes=("_old", "_new"), indicator=True
    )

    differences = comparison[comparison["_merge"] != "both"]

    return differences


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process DNA sequences, annotations, and perform searches.")
    parser.add_argument("--dna_seq", required=True, help="Path to the DNA sequence file in FASTA format.")
    parser.add_argument("--search_dict", required=True, help="Path to the search dictionary JSON file.")
    parser.add_argument("--old_annotation", required=True, help="Path to the old annotation file.")
    args = parser.parse_args()

    dna_sequence_file = args.dna_seq
    search_dict_file = args.search_dict
    old_annotation_file = args.old_annotation

    with open(search_dict_file, "r") as f:
        search_dict = json5.load(f)  # json5 supports comments natively

    with open(dna_sequence_file, "r") as file:
        record = next(SeqIO.parse(file, "fasta"))
        dna_sequence = str(record.seq)

    print("")
    print("********** Read in DNA Sequence")
    print("Länge DNA Seq: ", len(dna_sequence))

    domain_dna_file = "fetched_sequences.fasta"
    output_blast_file = "blast_results.txt"
    gtf_output_file = "annotations.gtf"

    # tested these for kyverna
    # KM595254.1 -> Synthetic construct 1-732 antibody light chain variable..
    # OP963038.1 -> Homo sapiens isolate Pfs230AL-30_HeavyChain immunoglobu..
    gene_ids = ["NM_001378516.1", "NM_171827.4", "NM_001561.6", "NM_001410981.1", "NR_027760.3"]
    print(f"Fetch nucleotide sequences from {gene_ids} from NCBI")
    gene_name_mapping = fetch_gene_names(gene_ids)
    fetch_fasta_from_ncbi(gene_ids, domain_dna_file)

    print("")
    print("********** Blast DNA Sequence to Fetched Proteins")
    dna_to_domain_blast(dna_sequence, domain_dna_file, output_blast_file, gtf_output_file, gene_name_mapping)
    print(f"GTF annotations saved to {gtf_output_file}")

    # Compare old and new annotations
    if os.path.getsize(gtf_output_file) > 0:
        print("")
        print("********** Compare old annotations with new annotations")
        differences = compare_annotations(old_annotation_file, gtf_output_file)
        if not differences.empty:
            print("Differences between old and new annotations:")
            print(differences)
        else:
            print("No differences found between old and new annotations.")
    else:
        print(f"New annotation file {gtf_output_file} is emtpy.")


    print("")
    print("********** Find Annotations (From patents) from JSON (based on nucleotide sequence) in DNA Seq")
    positions = find_flexible_substring_positions(dna_sequence, search_dict)
    print("Substring positions found:")
    for pos in positions:
        print(f"Name: {pos['name']}, Start: {pos['start']}, End: {pos['end']}, Substring: {pos['substring']}")
