from collections import namedtuple
lst = []
ls = ['surname', 'mark']
Inform = namedtuple('Inform', ls)
n = int(input())
for i in range(n):
    tmpData = input().split()
    info = Inform(tmpData[0], int(tmpData[1]))
    lst.append(info)
lst.sort(key=lambda a: a.mark, reverse=True)
print(*[i.surname for i in lst], sep='\n')
