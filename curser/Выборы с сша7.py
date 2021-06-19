vote = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        party, count = line.rstrip().split()
        vote[party] = vote.get(party, 0) + int(count)
print(*[k + ' ' + str(vote[k]) for k in sorted(vote)], sep='\n')
