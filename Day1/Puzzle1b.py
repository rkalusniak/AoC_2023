"""
Created: March 26 20:17 2024

by: Rachel Kalusniak
"""
from word2number import w2n
import re

# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_testb.txt'
else:
    data_file = 'input.txt'

# Open text file
with open(data_file, 'r') as f:
    input = f.read().splitlines()

# Detect numbers in the string
# Create pattern and add ?= for overlap
num_pattern = '(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
compile_pattern = re.compile(num_pattern)

# Find all numbers and number words and convert to integer
numbers = [[w2n.word_to_num(x) for x in re.findall(num_pattern, i)] for i in input]

# Find two-digit numbers with first and last value
two_digit = []
for j in numbers:
    two_digit.append(j[0]*10 + j[-1])

# # Find the sum of two digit list
print(sum(two_digit))