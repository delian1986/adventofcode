f = open("01_full.txt", "r")
input = f.read().splitlines()

col1 = []
col2 = []
distances = []

for line in input:
    col1.append(line.split()[0])
    col2.append(line.split()[1])

col1 = sorted(col1)
col2 = sorted(col2)

for i in range(len(col1)):
    distances.append(abs(int(col1[i]) - int(col2[i])))

print(sum(distances))



