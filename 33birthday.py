# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list


"""
python3 33birthday.py 365 23
0.571
"""

import sys

#num_people = 23
#num_days = 365

num_days = int(sys.argv[1])
num_people = int(sys.argv[2])

"""
fact = 1
fact2 = 1
for i in range(1,num_people):
    fact *= i

for j in range(1, (num_people-2)):
    fact2 *= j

combinations = fact / (2*fact2)   
"""

combi = (num_people-1) * num_people /2 #nC2

prob = 1 - ((num_days -1)/num_days)**combi

print("%.3f" % prob)