# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

f = open("06.txt", "r")
input = f.read()

items = list(input)
start = 0

while(1):

    slice = items[start:start + 4]

    unique = set(slice)

    if len(unique) == 4:
        break

    start +=1

print(start + 4)
exit
    
    