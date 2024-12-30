def setArea(start, end):
    list_area = set()
    for i in range(start, end + 1):
        list_area.add(i)

    return list_area


f = open("04.txt", "r")
input = f.read().splitlines()

# input = '''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''.splitlines()


found_overlap = 0
for pair in input:
    elven_pairs = pair.split(',')
    pair_1 = elven_pairs[0].split('-')
    pair_2 = elven_pairs[1].split('-')

    pair_1_area = setArea(int(pair_1[0]), int(pair_1[1]))
    pair_2_area = setArea(int(pair_2[0]), int(pair_2[1]))


    if pair_1_area.issubset(pair_2_area):
        found_overlap += 1
    elif pair_2_area.issubset(pair_1_area):
        found_overlap += 1

print(found_overlap)







        
