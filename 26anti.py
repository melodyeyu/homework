dna = "ACTGAAAAAAAAAAA"
revDNA = ""
for i in range(len(dna)-1, -1, -1):
	if dna[i] == "A":
		revDNA += "T"
	elif dna[i] =="G":
		revDNA += "C"
	elif dna[i] == "C":
		revDNA += "G"
	elif dna[i] == "T":
		revDNA += "A"

print(revDNA)
