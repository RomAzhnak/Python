from math import ceil
parties = []
votes = []
with open('input.txt', 'r', encoding='utf-8') as f:
    f.readline()
    line = f.readline().strip()
    while line != 'VOTES:' and line != '':
        parties.append(line)
        votes.append(0)
        line = f.readline().strip()
    for line in f:
        line = line.strip()
        votes[parties.index(line)] += 1
# print(*[parties[i] for i in range(len(votes)) if votes[i] >= ceil(sum(votes) * 7 / 100)], sep='\n')
border = ceil(sum(votes) * 7 / 100)
for i in range(len(votes)):
    print(parties[i]) if votes[i] >= border else None


# второй вариант
with open('input.txt', 'r', encoding='utf-8') as f:
    a, s, p = f.readlines(), 0, []
for i in a:
    p = [[a[i], 0] for i in range(1, a.index('VOTES:\n'))]
for i in range(len(p)):
    p[i][1] = a.count(p[i][0]) - 1
    s += p[i][1]
for i in range(len(p)):
    print(p[i][0].strip()) if p[i][1] / s * 100 >= 7 else None
