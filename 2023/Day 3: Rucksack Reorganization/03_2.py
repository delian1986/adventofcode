f = open("03_input.txt", "r")
input = f.read().splitlines()

# input = '''vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw'''.splitlines()

badges = list()

while len(input) > 0:
    group = input[0:3]
    del input[0:3]

    occurences = 0
    for letter_1 in group[0]:
        for letter_2 in group[1]:
            for letter_3 in group[2]:
                if letter_1 == letter_2 == letter_3:
                    occurences += 1

        if occurences >= 1:
            badges.append(letter_1)
            break

total_sum = 0
for found_occurencies in badges:
    if found_occurencies.isupper():
        total_sum += ord(found_occurencies) - 38
    else:
        total_sum += ord(found_occurencies) - 96

print(total_sum)

