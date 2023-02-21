# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane


"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
import mcb185
import sys

def kd(asequence):
	hydrophobicity = 0
	for aa in asequence:
		if	aa == 'A': hydrophobicity += 1.8
		elif aa == 'C': hydrophobicity += 2.5
		elif aa == 'D': hydrophobicity += -3.5
		elif aa == 'E': hydrophobicity += -3.5
		elif aa == 'F': hydrophobicity += 2.8
		elif aa == 'G': hydrophobicity += -0.4
		elif aa == 'H': hydrophobicity += -3.2
		elif aa == 'I': hydrophobicity += 4.5
		elif aa == 'K': hydrophobicity += -3.9
		elif aa == 'L': hydrophobicity += 3.8
		elif aa == 'M': hydrophobicity += 1.9
		elif aa == 'N': hydrophobicity += -3.5
		elif aa == 'P': hydrophobicity += -1.6
		elif aa == 'Q': hydrophobicity += -3.5
		elif aa == 'R': hydrophobicity += -4.5
		elif aa == 'S': hydrophobicity += -0.8
		elif aa == 'T': hydrophobicity += -0.7
		elif aa == 'V': hydrophobicity += 4.2
		elif aa == 'W': hydrophobicity += -0.9
		elif aa == 'Y': hydrophobicity += -1.3
	return hydrophobicity/len(asequence)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline, kd(seq[0:30]))
