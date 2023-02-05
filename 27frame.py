dna = 'ATGGCCTTT'
frame = 0

print("\"\"\"")
for position in range(0, len(dna), 3):
	for frame in range(3):
		print(position + frame, frame, dna[position+frame])
print("\"\"\"")