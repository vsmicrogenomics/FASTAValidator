"""
validateFASTA.py

This script processes the output files of AMRFinderPlus and generates a binary matrix
that shows the presence or absence of antibiotic resistance genes, stress response
genes, and virulence genes in each sample.

Written by Vikas Sharma, 2023
"""


import argparse

def is_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        in_sequence = False  # Whether we're currently reading a sequence
        sequence_empty = True  # Whether the current sequence is empty
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('>'):  # Description line
                if in_sequence and sequence_empty:  # Previous sequence was empty
                    return False
                in_sequence = True
                sequence_empty = True
            else:  # Sequence line
                valid_chars = set('ACTGactgNRYSWKMBDHVnryswkmbdhv')
                if not all(char in valid_chars for char in stripped):
                    return False
                sequence_empty = False  # We've read some characters for the current sequence
        if in_sequence and sequence_empty:  # Last sequence was empty
            return False
    return True

parser = argparse.ArgumentParser(description='Validate FASTA files.')
parser.add_argument('filenames', type=str, nargs='+', help='The names of the files to validate.')

args = parser.parse_args()

for filename in args.filenames:
    try:
        if not is_fasta(filename):
            raise ValueError(f'The file {filename} is not a valid FASTA file.')
    except ValueError as e:
        print(e)
