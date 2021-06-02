from operator import itemgetter
n = int(input())
s = list(map(int, input().split()))
towns = []
for i in range(n):
    towns.append((i+1, s[i]))
towns.sort(key=itemgetter(1))
print(towns)
n = int(input())
# bom = list(enumerate(map(int, input().split()), start=1))[:n]
s = list(map(int, input().split()))
bom = []
for i in range(n):
    bom.append([i+1, s[i]])
bom.sort(key=itemgetter(1))
lst = []
nex = 0
for i in range(len(towns)):
    dist = abs(towns[i][1] - bom[nex][1])
    lst.append((towns[i][0], bom[nex][0]))
    for j in range(nex+1, len(bom)):
        if dist > abs(towns[i][1] - bom[j][1]):
            dist = abs(towns[i][1] - bom[j][1])
            lst[i] = (towns[i][0], bom[j][0])
            nex = j
        else:
            break
lst.sort(key=itemgetter(0))
print(*[lst[i][1] for i in range(len(lst))])
# ls = [lst[i][1] for i in range(len(lst))]
# print(*ls)

# второй вариант
n = int(input())
town = list(enumerate(map(int, input().split())))[:n]
m = int(input())
bom = list(enumerate(map(int, input().split())))[:m]
town.sort(key=lambda p: p[1])
bom.sort(key=lambda p: p[1])
j = 0
ans = []
for i in range(n):
    while j != m-1 and abs(town[i][1]-bom[j][1]) > abs(town[i][1]-bom[j+1][1]):
        j += 1
    else:
        ans.append([bom[j][0] + 1, town[i][0]])
ans.sort(key=lambda p: p[1])
print(*[ans[i][0] for i in range(len(ans))])
# print(*ls)
