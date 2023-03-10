# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
import sys
import math
import mcb185

filename ='/Users/melodyyu/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz'
#filename = sys.argv[1]
window = 11
#window = int(sys.argv[2])
threshold = 1.4
#threshold = float(sys.argv[3])

def entropy(probabilities):
	entropy = 0.0
	for p in probabilities:
		if p > 0:
			entropy -= p * math.log2(p)
	return entropy

def probabilities(sequence):
	l = len(sequence)
	prob = [sequence.count('A')/l, sequence.count('C')/l, sequence.count('T')/l, sequence.count('G/')/l]
	return prob
 


for defline, seq in mcb185.read_fasta(filename):
	words = defline.split()
	name = words[0]
#tested w range(300) len(seq)-1
finalsequence = ''
for i in range(300):
	pbs = probabilities(seq[i:window+i-1])
	if (entropy(pbs) < threshold):
		finalsequence += 'N'
	else:
		finalsequence += seq[i]

print(name)
segments = [finalsequence[i:i+59] for i in  range(0, len(finalsequence), 60)]

for seg60 in segments:
	print(seg60)

