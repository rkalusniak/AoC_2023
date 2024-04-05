"""
Created: April 4 23:23 2024

by: Rachel Kalusniak
"""
import pandas as pd
import re
from operator import itemgetter
from itertools import groupby

# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'

# Open text file
with open(data_file, 'r') as f:
    input = f.read().splitlines()

# Initialize lists to hold pulls and games
game_num_ls = []
pull_num_ls = []
pull_value_ls = []

# Loop through each line/game
for i in range(0, len(input)):

    # Split out the pulls from the game number
    split_game = [x.strip() for x in re.split(':', input[i])]

    # Split each game
    game_ls = [x.strip() for x in re.split(';', split_game[1])]

    # Loop through each pull
    for j in range(0, len(game_ls)):

        # Split each pull into the pull part
        pull_part = [x.strip() for x in re.split(',', game_ls[j])]

        # Loop through each pull color
        for k in range(0, len(pull_part)):
            game_num_ls.append(i + 1)  # Record the game number
            pull_num_ls.append(j)  # Record the pull number
            pull_value_ls.append(pull_part[k])  # Record the pull vale


# Combine lists into pandas dataframe
game_df = pd.DataFrame({'game': game_num_ls,
                        'pull_number': pull_num_ls,
                        'pull_value': pull_value_ls})

# Split the pull value into number and color
game_df[['pull_count', 'pull_color']] = game_df['pull_value'].str.split(' ', expand=True)

# Convert the pull number into an integer
game_df['pull_count'] = pd.to_numeric(game_df['pull_count'])

# Remove pull_value column because no longer needed
game_df = game_df.drop('pull_value', axis=1)
game_df = game_df.drop('pull_number', axis=1)

# Group by game number and pull color to find the min number for each game
gamemax_df = pd.DataFrame(game_df.groupby(['game', 'pull_color']).max().reset_index())

# Find the product when group by game
product_ls = list(gamemax_df.groupby('game')[['pull_count']].prod()['pull_count'])

# Find the sum of the products
print(sum(product_ls))


