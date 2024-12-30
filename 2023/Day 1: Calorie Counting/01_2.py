f = open("01_input.txt", "r")
input = f.read().splitlines()

elves = list()

current_sum = 0

for calories in input:
    if calories != '':
        current_sum += int(calories)
    else:
        elves.append(current_sum)

        current_sum = 0

elves.sort(reverse=True)
print(sum(elves[0:3]))
