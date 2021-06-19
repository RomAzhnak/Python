from operator import itemgetter


wcount = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tData = line.split()
        for elem in tData:
            wcount[elem] = wcount.get(elem, 0) + 1
print(max(sorted(wcount), key=lambda x: wcount[x]))
print(max(sorted(wcount.items()), key=lambda x: x[1])[0])
"""wcount = sorted(wcount.items(), itemgetter(0))+
tData = max(wcount, key=itemgetter(1))    можно так
print(tData[0])
wcount.sort(key=itemgetter(1), reverse=True)"""
#wcount = sorted(wcount.items(), key=lambda x: (-x[1], x[0]))
#print(wcount[0][0])
print(sorted(wcount))
