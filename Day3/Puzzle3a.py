"""
Created: April 17:23 2024

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


# Get all types of special characters
# Initialize list for special characters
special_ls = []

# Find non-number or period values
for line in input:
    special_ls.append(re.findall(r'[^\.0-9]+', line))

# Convert list of list duplicates to regex string to match
# Flatten and remove duplicates
special_set = {x for l in special_ls for x in l}

# Initialize string
special_str = ''

# Loop through list and add escape character before each
for char in special_set:
    special_str += '\\' + char

# Add outside brackets
special_str = '[' + special_str + ']'


# Find the line start and end location of matches
# Initialize list and counter
all_matches = []
i = 0

# Compile the pattern to match
match_pattern = re.compile(r'\d{1,3}')

# Loop through lines to record start and end location of numbers
for i in range(0, len(input)):
    for match in re.finditer(match_pattern, input[i]):
        s = match.start()               # Start location
        e = match.end()                 # End location
        all_matches.append([i, s, e])   # Add line number, start, and end to list
    i += 1                              # Iterate to next line


# Record the size of the input
input_size = len(input)

# Create the match pattern
print(special_str)
special_pattern = re.compile(special_str)

# Initialize list to hold matches
match_num = []

# Loop through each location to test
for location in all_matches:

    # Initialize string of touching characters
    test_str = ""

    # Convert list locations to easy names
    row = location[0]
    start = location[1]
    end = location[2]

    # Get the top values
    if row > 0:
        test_str += input[row-1][start:end]

    # Get bottom values
    if row < input_size-1:
        test_str += input[row+1][start:end]

    # Get left  and left diagonals
    if start > 0:
        test_str += input[row][start-1]           # same line
        if row > 0:
            test_str += input[row-1][start-1]     # top diagonal
        if row < input_size-1:
            test_str += input[row+1][start-1]     # bottom diagonal

    # Get right value and right diagonals
    if end < input_size-1:
        test_str += input[row][end]               # same line
        if row > 0:
            test_str += input[row-1][end]         # top diagonal
        if row < input_size-1:
            test_str += input[row+1][end]         # bottom diagonal

    # See if the test string has special characters
    if re.search(special_pattern, test_str):
        match_num.append(int(input[row][start:end]))

# Print the answer by summing list
print(match_num)

print(f'The answer is {sum(match_num)}')
