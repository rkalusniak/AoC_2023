"""
Created: April 1 18:02 2024

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

# Group by game number and pull color to find the max number for each game
gamemax_df = pd.DataFrame(game_df.groupby(['game', 'pull_color']).max().reset_index())


# Create list of criteria
criteria_ls = [[12, 13, 14], ['red', 'green', 'blue']]

# Initialize list of overage games
overage_games = []

# Loop through the criteria list
for i in range(0, len(criteria_ls) + 1):

    # Create a list of all game that are greater than the criteria and not possible
    overage_games.append(list(gamemax_df['game'][(gamemax_df['pull_count'] > criteria_ls[0][i]) & (
                gamemax_df['pull_color'] == criteria_ls[1][i])]))

# Flatten the list of overage games
flat_overage_games = [val for sublist in overage_games for val in sublist]

# Record unique games and unique games over the criteria
unique_overage_games = list(set(flat_overage_games))
unique_games = list(game_df['game'].unique())

# Find the sum of game numbers that meet the criteria
print(sum(unique_games) - sum(unique_overage_games))
