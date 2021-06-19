from collections import namedtuple
lst = []
ls = ['surname', 'name', 'clas', 'mark']
Inform = namedtuple('Inform', ls)
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tmpData = line.split()
        info = Inform(tmpData[0], tmpData[1], int(tmpData[2]), int(tmpData[3]))
        lst.append(info)
maxMark = []
for j in range(9, 12):
    maxMark.append(max([i.mark for i in lst if i.clas == j]))
print(*maxMark)
