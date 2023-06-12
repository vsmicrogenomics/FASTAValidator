# FASTAValidator
FASTAValidator: A Python script for validating FASTA files by checking their format and sequence content

A Python script to validate FASTA files by checking their format and content.

The script uses the argparse module to handle command-line arguments. It defines a function, is_fasta(), which takes a filename as input and determines if the file is a valid FASTA file. The function reads the file, line by line, and checks if the lines follow the FASTA format rules.

The FASTA format consists of one or more sequences, where each sequence begins with a description line starting with '>'. The description line is followed by one or more lines containing the sequence itself. The sequence lines can only contain valid characters, which are a combination of uppercase and lowercase letters ('A', 'C', 'T', 'G', 'a', 'c', 't', 'g') and special characters ('N', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'n', 'r', 'y', 's', 'w', 'k', 'm', 'b', 'd', 'h', 'v').

The sequence characters "ACTGactgNRYSWKMBDHVnryswkmbdhv" represent the valid characters allowed in a FASTA sequence. Here is an explanation of each character:

A, C, T, G: These represent the four nucleotide bases found in DNA: Adenine, Cytosine, Thymine, and Guanine.
a, c, t, g: These represent the same nucleotide bases but in lowercase.
N: Represents any nucleotide base, indicating ambiguity or uncertainty.
R: Represents a purine base, which can be either A (adenine) or G (guanine).
Y: Represents a pyrimidine base, which can be either C (cytosine) or T (thymine).
S: Represents a strong base, which can be either C (cytosine) or G (guanine).
W: Represents a weak base, which can be either A (adenine) or T (thymine).
K: Represents a keto base, which can be either G (guanine) or T (thymine).
M: Represents an amino base, which can be either A (adenine) or C (cytosine).
B: Represents any base except A (adenine).
D: Represents any base except C (cytosine).
H: Represents any base except G (guanine).
V: Represents any base except T (thymine).
n, r, y, s, w, k, m, b, d, h, v: These represent the same bases as their uppercase counterparts but in lowercase.

If the file does not adhere to the FASTA format rules, the script returns False. Otherwise, it returns True.

To use the script, provide one or more filenames as command-line arguments. The script will attempt to validate each file and display an error message if any of them are not valid FASTA files.

Example usage:
python validateFASTA.py file1.fasta

Citations
If you are using the validateFASTA.py script, please cite it as follows: Sharma, V. (2023). validateFASTA.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/FASTAValidator

