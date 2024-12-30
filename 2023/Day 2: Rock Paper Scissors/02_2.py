f = open("02.txt", "r")
input = f.read().splitlines()

# input = '''A Y
# B X
# C Z'''.splitlines()


data = {
    'Y' : 'draw',
    'X' : 'lose',
    'Z' : 'wins'
}

elven_items = {
    'A' : { #rock
        'Y' : 'X', #draw
        'Z' : 'Y', #wins
        'X' : 'Z' #lose
    },
    'B' : { #paper
        'Y' : 'Y', #draw
        'Z' : 'Z', #wins
        'X' : 'X' #lose
    },
    'C' : { #scissor
        'Y' : 'Z', #draw
        'Z' : 'X', #wins
        'X' : 'Y' #lose
    }

}

my_items = {
    'X': { # rock
        'points' : 1
    },
    'Y' : { #paper
        'points' : 2
    },
    'Z' : { #scissor
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
    action = choices[1]

    item_should_i_play = elven_items[enemy_choice][action]
    
    points_of_item_i_played = my_items[item_should_i_play]['points']
    points_of_outcome = score[data[action]]

    total += points_of_item_i_played + points_of_outcome




print(total)
