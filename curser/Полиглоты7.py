langSet1 = set()
langSet2 = set()
with open('input.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        m = int(f.readline())
        tmpLine = set()
        for j in range(m):
            tmpLine.add(f.readline().strip())
        langSet1.update(tmpLine)
        if i == 0:                  # if ... else... заменяется на:
            langSet2 = tmpLine      # langSet2 = langSet2 & tmpLine if i else tmpLine
        else:
            langSet2 &= tmpLine
print(len(langSet2), *langSet2, sep='\n')
print(len(langSet1), *langSet1, sep='\n')

# второй вариант
totalLangs, allLangs = set(), set()
for i in range(int(input())):
    langs = set(input() for _ in range(int(input())))
    totalLangs |= langs
    allLangs = allLangs & langs if i else langs
print(len(allLangs), '\n'.join(allLangs), sep='\n')
print(len(totalLangs), '\n'.join(totalLangs), sep='\n')
