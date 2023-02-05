import random
length = 30
dna = ""
dnapool = ["A", "C", "G", "T"]
ATcount = 0

print("\"\"\"")
for i in range(30):
	j = random.randint(0,30)
	if j<=20:
		dna = dna + random.choice("AT")
		ATcount += 1
	else:
		dna = dna + random.choice("GC")

print(length, ATcount/length, dna)
print("\"\"\"")
