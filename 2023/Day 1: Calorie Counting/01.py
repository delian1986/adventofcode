f = open("01_input.txt", "r")
input = f.read().splitlines()

max_calories = 0
current_sum = 0

for calories in input:
    if calories != '':
        current_sum += int(calories)
    else:
        if current_sum > max_calories :
            max_calories = current_sum

        current_sum = 0 

print(max_calories)
