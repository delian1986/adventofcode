# input = '''move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''.splitlines()

# crates = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['P']
# ]


f = open("05.txt", "r")
input = f.read().splitlines()

crates = [
    ['Z','J','N','W','P','S'],
    ['G','S','T'],
    ['V','Q','R','L','H'],
    ['V','S','T','D'],
    ['Q','Z','T','D','B','M','J'],
    ['M','W','T','J','D','C','Z','L'],
    ['L','P','M','W','G','T','J'],
    ['N','G','M','T','B','F','Q','H'],
    ['R','D','G','C','P','B','Q','W']
]


for move in input:
    instructions = move.split(' ')

    move_count = int(instructions[1])
    start = int(instructions[3]) - 1
    end = int(instructions[5]) - 1

    items = crates[start][-move_count:]

    for item in items[::-1]:
        del(crates[start][-1])

        crates[end].append(item)

    
result = ''
for index in range(len(crates)):
    result += crates[index].pop(-1)
print(result)
exit()

