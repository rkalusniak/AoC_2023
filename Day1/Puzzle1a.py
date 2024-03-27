"""
Created: March 26 06:31 2024

by: Rachel Kalusniak
"""
import re

# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'

# Open text file
with open(data_file, 'r') as f:
    input = f.read().splitlines()

# Find the all the numbers in string and convert to numeric
numbers = [[int(x) for x in re.findall("\d", i)] for i in input]

# Find two-digit numbers with first and last value
two_digit = []
for j in numbers:
    two_digit.append(j[0]*10 + j[-1])

# Find the sum of two digit list
print(sum(two_digit))