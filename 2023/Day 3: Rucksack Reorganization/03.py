f = open("03_input.txt", "r")
input = f.read().splitlines()

# input = '''vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw'''.splitlines()

# print(ord('Z') - 63)

# exit()


item_rearrangement = list()

for item in input:
    item_length = len(item)
    split_point = int(item_length / 2)

    first_compartment = item[0 : split_point]
    second_compartment = item[split_point :]

    for letter_in_first in first_compartment:
        occurence = 0

        for letter_in_second in second_compartment:
            if letter_in_first == letter_in_second:
                occurence += 1
    
        if occurence >= 1:
            item_rearrangement.append(letter_in_first)
            break

total_sum = 0
for found_occurencies in item_rearrangement:
    if found_occurencies.isupper():
        total_sum += ord(found_occurencies) - 38
    else:
        total_sum += ord(found_occurencies) - 96

print(total_sum)

