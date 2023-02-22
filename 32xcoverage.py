# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""

import random
import string

numb_of_fragments = 10
fragments = []


min = 999999999
max = 0
DNA = "";

for i in range(numb_of_fragments-1):
	fragments += [''.join(  random.choices("ACGT", k=10))]

for i in range(numb_of_fragments-1):
	# compare with n-1 fragments if there is a match
	for j in range(i, (numb_of_fragments-1)):
		if (fragments[i].substring(fragments[j])):
			print ("join the two strings and assign to DNA")
#print (fragments) 