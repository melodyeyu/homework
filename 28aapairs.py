AA = "ACDEFGHIKLMNPQRSTVWY"
combinations = 0

for i in range(len(AA)):
	for j in range(len(AA) - i):
		if(AA[i] !=AA[i+j]):
			print(AA[i]+ " " + AA[i + j])
			combinations += 1
print(combinations)

