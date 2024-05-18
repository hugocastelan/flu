from Bio import SeqIO
import re

def read_pattern_file(pattern_file):
    """
    Lee el archivo de patrón y devuelve su contenido como una lista de patrones.
    :param pattern_file: El archivo que contiene los patrones de búsqueda.
    :return: Una lista de patrones de búsqueda.
    """
    patterns = []
    with open(pattern_file, "r") as file:
        for line in file:
            patterns.append(line.strip())
    return patterns

def grep_sequences(fasta_file, pattern_file, output_file):
    """
    Extrae las secuencias cuyos identificadores coinciden con los patrones dados en el archivo de patrón y las guarda en un archivo de salida.
    :param fasta_file: El archivo multifasta del cual extraer las secuencias.
    :param pattern_file: El archivo que contiene los patrones de búsqueda.
    :param output_file: El archivo de salida donde se guardarán las secuencias correspondientes.
    """
    patterns = read_pattern_file(pattern_file)
    print(len(patterns), "patrones cargados desde el archivo.")

    with open(output_file, "w") as out_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            for pattern in patterns:
                if re.search(pattern, record.id):
                    SeqIO.write(record, out_file, "fasta")
                    break

# Ejemplo de uso
fasta_file = "/Users/hugo/Desktop/Test_HA_PA/BVBRC_genome_sequence.fasta"  # Reemplaza con la ruta de tu archivo multifasta
pattern_file = "/Users/hugo/Desktop/Test_HA_PA/HA_headers_bvbrc.txt"  # Reemplaza con la ruta de tu archivo de patrones
output_file = "/Users/hugo/Desktop/Test_HA_PA/HA_headers_bvbrc.fasta"  # Reemplaza con la ruta del archivo de salida

grep_sequences(fasta_file, pattern_file, output_file)
print("Secuencias correspondientes a los patrones de búsqueda guardadas en", output_file)
