f = open("01_2_full.txt", "r")
input = f.read().splitlines()

col1 = []
col2 = []
total_distance = 0

for line in input:
    col1.append(line.split()[0])
    col2.append(line.split()[1])

for i in range(len(col1)):
    curr_num = int(col1[i])
    found_times = 0

    for j in range(len(col2)):
        if curr_num == int(col2[j]):
            found_times += 1

    total_distance += found_times * curr_num

print(total_distance)
