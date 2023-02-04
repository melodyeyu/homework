dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
total = len(dna)
gc = 0
for i in dna:
	if i == "C" or i == "G":
		gc = gc + 1
print("%.2f" % (gc/total))