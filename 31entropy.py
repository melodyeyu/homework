# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
import sys
import math

args = sys.argv
numbers = args[1:]



try:
	numbers = [float (i) for i in numbers]
except:
	print(f'Arguments must contain only numbers', file=sys.stderr)
	raise

#if (sum(numbers) != 1.0):

try:
	assert(math.isclose(sum(numbers), 1.0))
except:
	sys.exit("probabilites do not sum to 1.0")

entropy = 0.0
for p in numbers:
	if p > 0:
		entropy -= p * math.log2(p)
		
print("%.3f" % entropy)
	