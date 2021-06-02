wcount = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for elem in line.split():
            wcount[elem] = wcount.get(elem, 0) + 1
# tup = [(y, x) for x, y in sorted(wcount.items())]
# tup = sorted(tup, key=lambda x: x[0],  reverse=True)
wcount = sorted(wcount.items(), key=lambda x: (-x[1], x[0]))
print(*[x[0] for x in wcount], sep='\n')
