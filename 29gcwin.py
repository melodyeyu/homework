seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
gcCount = 0

for i in range(len(seq)-w):
	gcCount = 0
	for nt in seq[i:i+w]:
		if nt == "G" or nt == "C":
			gcCount +=1
	print(i, end= " ")
	print(seq[i:i+w], end=" ")
	print("%.4f" % (gcCount/w))