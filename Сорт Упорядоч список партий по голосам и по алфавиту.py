from operator import itemgetter
with open('input.txt', 'r', encoding='utf-8') as f:
    s, votes = f.readlines(), []
for i in s:
    votes = [[s[i], 0] for i in range(1, s.index('VOTES:\n'))]
for i in range(len(votes)):
    votes[i][1] = s.count(votes[i][0]) - 1
votes.sort(key=itemgetter(0))
votes.sort(key=itemgetter(1), reverse=True)
# votes.sort(key=lambda x: (-x[1], x[0]))   # та же сортировка по двум параметрам
print(*[votes[i][0].strip() for i in range(len(votes))], sep='\n')
