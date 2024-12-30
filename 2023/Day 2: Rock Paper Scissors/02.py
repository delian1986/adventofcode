f = open("02.txt", "r")
input = f.read().splitlines()

# input = '''A Y
# B X
# C Z'''.splitlines()

config = {
    'X': { # rock
        'C' : 'wins',
        'A' : 'draw',
        'B' : 'lose',
        'points' : 1
    },
    'Y' : { #paper
        'A' : 'wins',
        'B' : 'draw',
        'C' : 'lose',
        'points' : 2
    },
    'Z' : { #scissor
        'B' : 'wins',
        'C' : 'draw',
        'A' : 'lose',
        'points' : 3
    },
}

score = {
    'lose' : 0,
    'draw' : 3,
    'wins' : 6
}

# print(config['X']['C'])


# exit()

total = 0 

for turn in input:
    choices = turn.split()
    enemy_choice = choices[0]
    my_choice = choices[1]

    round = config[my_choice][enemy_choice]
    points_of_choice = config[my_choice]['points']
    points_of_round = score[round]

    total += points_of_choice + points_of_round

print(total)
