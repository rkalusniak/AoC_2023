"""
Created: March 26 08:17 2024

by: Rachel Kalusniak
"""
import inflect
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

# Create an engine to read words to numbers
p = inflect.engine()

numbers = [[int(x) for x in re.findall("\d", i)] for i in input]

# Find two-digit numbers with first and last value
two_digit = []
for j in numbers:
    two_digit.append(j[0]*10 + j[-1])

# Find the sum of two digit list
print(sum(two_digit))

word = "three"
number = p.number_to_words(word)
print(number)