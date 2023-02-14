# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
import sys

args = sys.argv
#args = ["30stats.py", "3", "1", "4", "1", "5"]

numbers = args[1:]
numbers = [int (i) for i in numbers]
numbers.sort()

count = len(numbers)
min = numbers[0]
max = numbers[-1]
mean = sum(numbers)/count
 

variance = 0.0

for x in numbers:
    variance += (x-mean)**2

stddev = (variance/(count))**0.5

print("Count: %d" % count)
print("Minimum: %.1f" % min)
print("Maximum: %.1f" % max)
print("Mean: %.3f" % mean)
print("Std. dev: %.3f" % stddev)
print("Median: %.3f" % numbers[int(count/2)])