wcount = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tData = line.split()
        for elem in tData:
            print(wcount.get(elem, 0), end=' ')
            wcount[elem] = wcount.get(elem, 0) + 1
