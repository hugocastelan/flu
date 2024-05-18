def main():
    """
    This function reads 8 influenza virus gene sequences from FASTA files,
    concatenates each gene separately, and saves the concatenated whole genome sequence.
    """

    # Define directory containing the FASTA files
    directory = '/Volumes/Untitled/vaccine/'

    # List of gene filenames (modify if file names differ)
    gene_names = [
        'PB2',
        'PB1',
        'PA',
        'HA',
        'NP',
        'NA',
        'MP',
        'NS'
    ]

    # Initialize an empty dictionary to store gene sequences for each virus
    virus_sequences = {}

    # Loop through each gene
    for gene_name in gene_names:
        # Open the FASTA file for the current gene
        with open(directory + f'common_{gene_name}.fasta', 'r') as file:
            # Initialize virus_id outside the loop to handle unexpected line formats
            virus_id = None
            # Loop through each sequence in the file
            for line in file:
                # Check if this is a header line
                if line.startswith('>'):
                    # Extract the virus ID from the header
                    parts = line.strip().split('|')
                    if len(parts) >= 3:
                        virus_id = parts[2]
                    else:
                        print(f"Advertencia: La línea no tiene el formato esperado: {line}")
                elif virus_id is not None:  # Only concatenate if virus_id is defined
                    # Concatenate the sequence to the appropriate gene for this virus
                    virus_sequences.setdefault(virus_id, {}).setdefault(gene_name, '')
                    virus_sequences[virus_id][gene_name] += line.strip()

    # Define output filename for the concatenated whole genome sequences
    output_file = 'concatenated_whole_genome.fasta'

    # Write concatenated sequences to the output file
    with open(directory + output_file, 'w') as file:
        # Loop through each virus and write its concatenated sequence
        for virus_id, gene_sequences in virus_sequences.items():
            # Write header line for this virus
            file.write(f'>{virus_id}\n')
            # Concatenate sequences for each gene and write to file
            concatenated_sequence = ''.join(gene_sequences.get(gene_name, '') for gene_name in gene_names)
            file.write(concatenated_sequence + '\n')

if __name__ == "__main__":
    main()
