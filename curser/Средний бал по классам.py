from collections import namedtuple
lst = []
ls = ['surname', 'name', 'clas', 'mark']
Inform = namedtuple('Inform', ls)
with open('input.txt', 'r', encoding='utf-8') as f:
#    lines = f.readlines()
    for line in f:
        tmpData = line.split()
        info = Inform(tmpData[0], tmpData[1], int(tmpData[2]), int(tmpData[3]))
        lst.append(info)
lst.sort(key=lambda a: a.clas)
avgMark = []
for j in range(9, 12):
    tmpData = [i.mark for i in lst if i.clas == j]
    if len(tmpData) == 0:
        avgMark.append(0.0)
    else:
        avgMark.append(sum(tmpData) / len(tmpData))
print(*avgMark)
