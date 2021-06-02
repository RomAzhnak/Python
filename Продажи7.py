"""customer, product, s = {}, {}, ''
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        key = line[0] + ' ' + line[1]
        product[key] = product.get(key, 0) + int(line[2])
for key in sorted(product.items()):
    if key[0].split()[0] != s:
        print(key[0].split()[0]+':')
        s = key[0].split()[0]
    print(key[0].split()[1] + ' ' + str(key[1]))
"""

# второй вариант
word = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a = line.split()
        word.setdefault(a[0], dict())   # word[a[0]] = word.get(a[0], dict())
        word[a[0]][a[1]] = word[a[0]].get(a[1], 0) + int(a[2])
for i in sorted(word):
    print(i + ':')  # print(f'{i}:')
    [print(j, word[i][j]) for j in sorted(word[i])]

# подробно
fin = open('input.txt', 'r', encoding='utf-8')

mainDict = {} # единственный словарь, где хранится всё
              # {cusomer1: {
              #     product1: 12,
              #     product2: 7,
              #     ...}
              #  customer2: {
              #     product3: 3,
              #     product4: 9
              #     ...}
              #  ...
              #  }
for line in fin:
    listLine = line.strip().split()
    cust = listLine[0]       # покупатель
    prod = listLine[1]       # продукт
    coun = int(listLine[2])  # кол-во
    mainDict[cust] = mainDict.get(cust, {})
    mainDict[cust][prod] = mainDict[cust].get(prod, 0) + coun
for entry in sorted(mainDict):  # обходим словарь и печатаем
    print(entry, ':', sep='')
    for entry2 in sorted(mainDict[entry]):
        print(entry2, mainDict[entry][entry2])
