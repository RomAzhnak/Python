wcount = {}
allv = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        wcount[line.strip()] = wcount.get(line.strip(), 0) + 1
        allv += 1
wc = sorted(wcount.items(), key=lambda x: x[1], reverse=True)
with open('output.txt', 'w', encoding='utf-8') as f:
    if wc[0][1] >= allv // 2 + 1:
        print(wc[0][0], sep='\n', file=f)
    else:
        print(wc[0][0], wc[1][0], sep='\n', file=f)

# второй вариант
word = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
    for line in a:
        word[line] = word.get(line, 0) + 1
print(a)
b = [[i.strip(), word[i]] for i in sorted(word, key=word.get, reverse=True)]
with open('output.txt', 'w', encoding='utf-8') as f:
    print(b[0][0], file=f) if len(a) / b[0][1] < 2 else print(b[0][0], b[1][0], sep='\n', file=f)
