# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

f = open("06.txt", "r")
input = f.read()

items = list(input)
start = 0

while(1):

    slice = items[start:start + 14]

    unique = set(slice)

    if len(unique) == 14:
        break

    start +=1

print(start + 14)
exit