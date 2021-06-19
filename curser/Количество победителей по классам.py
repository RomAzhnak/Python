lst = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tmpData = line.split()
        lst.append([int(tmpData[2]), int(tmpData[3])])
maxMark = [0]*3
for j in range(9, 12):
    maxTmp = max([i[1] for i in lst if i[0] == j])
    print([i[1] for i in lst if i[0] == j].count(maxTmp), end=' ')
#    maxMark[j-9] = [i[1] for i in lst if i[0] == j].count(maxTmp)
# print(*maxMark)
