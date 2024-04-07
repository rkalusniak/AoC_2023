"""
Created: April 17:23 2024

by: Rachel Kalusniak
"""

import re
import numpy as np

# Allow to run with test or actual file
test = True
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'

# Open text file
with open(data_file, 'r') as f:
    input = f.read().splitlines()

# Get output into numpy array
input_horizontal = np.array([list(x) for x in input])

# Record each column as an array
input_vertical = np.transpose(input_horizontal)


# Record the verticals as a list of lists
# Initialize list is diagonal results and get shape of input
diag_ls = []
input_size = input_horizontal.shape[0]

# Create a key list to track the position in the diagonals
nums_horizontal = np.arange(input_size*input_size).reshape((input_size, input_size))

#Create a list to test both the input and number keys
diag_names = ['input', 'nums']

# Record diagonal once for input and once for position key
for name in diag_names:
    # Initialize diagonal list
    input_diagonal = []

    # Create flipped array for opposite diagonals
    input_flip = np.fliplr(eval(name+'_horizontal'))

    # Loop to cover all lines of the array
    for i in range(0, input_size-1):
        input_diagonal.append(list(np.diag(eval(name+'_horizontal'), k = i)))
        input_diagonal.append(list(np.diag(input_flip, k=i)))

        # Avoid duplicates of the original zero array
        if i > 0:
            input_diagonal.append(list(np.diag(eval(name+'_horizontal'), k=-i)))
            input_diagonal.append(list(np.diag(input_flip, k = -i)))

    # Create a master list with the input and key lists
    diag_ls.append(input_diagonal)


# Get all types of special characters

# Initialize list for special characters
special_ls = []

# Find non-number or period values
for line in input:
    special_ls.append(re.findall(r'[^\.0-9]', line))

# Convert list of list duplicates to regex string ot match
special_set = {x for l in special_ls for x in l}    # Flatten list to unique set
special_str = ''.join(special_set)                  # Set to string
special_str = '[\\' + special_str + ']'             # Add brackets and escape characters



# Horizontal Match
match_parts = []
for input_strip in input_horizontal:
    input_str = ''.join(input_strip)
    match_parts.append(re.findall('(\d+)'+special_str, input_str))

match_parts = [val for sublist in match_parts for val in sublist]

# Vertical Match
match_vert = []
i = 0
d_start = re.compile('\d' + special_str)
d_end = re.compile(special_str + '\d')

for input_strip in input_vertical:
    input_str = ''.join(input_strip)

    match_vert.append([(m.start(), i) for m in d_start.finditer(input_str)])
    match_vert.append([(m.end()-1, i) for m in d_end.finditer(input_str)])
    i += 1

# Flatten list to include just matching coordinates
match_vert_loc = [val for sublist in match_vert for val in sublist]

# Find the number at the coordinates
for i in range(0, len(match_vert_loc)):
    row = match_vert_loc[i][0]
    column = match_vert_loc[i][1]
    input_str = ''.join(input_horizontal[row])

    match_parts.append(re.findall(r'\d{2,3}', input_str[column-2:])[0])

# for input_strip in input_horizontal:
#     input_str = ''.join(input_strip)
#     print(int(x) for x in re.findall('(\d+)'+special_str, input_str))

    #
    #     if (re.match(r'\d', input_strip[i]) and
    #         (re.match(special_str, input_strip[i+1]) or
    #          re.match(special_str, input_strip[i-1]))):
    #         print(input_str)

print(match_parts)
