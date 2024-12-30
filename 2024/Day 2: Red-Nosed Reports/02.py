f = open("sample.txt", "r")
input = f.read().splitlines()

count_of_safe = 0

for i in range(len(input)):
    report = input[i].split()
    is_asc = True if report[0] < report[1] else False

    is_safe = True
    for j in range(len(report)-1):
        curr_num = report[j]
        next_num = report[j+1]

        if is_asc:
            if curr_num <= next_num:
                diff = int(next_num) - int(curr_num)
                if diff < 1 or diff > 3:
                    is_safe = False
                    break
            else:
                is_safe = False
                break
        else:
            if curr_num >= next_num:
                diff = int(curr_num) - int(next_num)
                if diff < 1 or diff > 3:
                    is_safe = False
                    break
            else:
                is_safe = False
                break

    if is_safe:
        count_of_safe += 1

print(count_of_safe)



