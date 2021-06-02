lst = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tmpData = line.split()
        info = [int(tmpData[2]), int(tmpData[3])]
        lst.append(info)
avgMark = []
for j in range(9, 12):
    tmpData = [i[1] for i in lst if i[0] == j]
    if len(tmpData) == 0:
        avgMark.append(0.0)
    else:
        avgMark.append(sum(tmpData) / len(tmpData))
# print(*avgMark)
print('{:f}, {:.3f}, {:.2f}'.format(*avgMark))
# второй вариант
school = ([], [], [])
fin = open('input.txt', 'r', encoding='utf8')
for line in fin:
    line = line.split()
    c = int(line[2])
    school[c - 9].append(int(line[3]))
for c in school:
    print(sum(c) / len(c), end=' ')
print()
# еще
inFile = open('input.txt', 'r', encoding='utf8')
s = [0] * 12
m = [0] * 12
for line in inFile:
    l = line.split()
    m[int(l[2])] += 1
    s[int(l[2])] += int(l[3])
print(s[9] / m[9], s[10] / m[10], s[11] / m[11])
inFile.close()