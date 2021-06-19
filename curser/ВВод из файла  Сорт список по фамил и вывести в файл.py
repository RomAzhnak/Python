from collections import namedtuple
lst = []
ls = ['surname', 'name', 'school', 'mark']
Inform = namedtuple('Inform', ls)
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tData = line.split()
        if tData:
            info = Inform(tData[0], tData[1], int(tData[2]), int(tData[3]))
#            info = Inform(*tData)
            lst.append(info)
lst.sort(key=lambda a: a.surname)
with open('output.txt', 'w', encoding='utf-8') as f:
    for i in lst:
        print(i.surname, i.name, i.mark, file=f)

# второй вариант
a = open('input.txt', 'r', encoding='utf8')
b = open('output.txt', 'w', encoding='utf8')
m = []
for line in a:
    m.append(line.split())
m.sort()
for i in range(len(m)):
    print(*m[i][:2], m[i][3], file=b)
a.close()
b.close()
