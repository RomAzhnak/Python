import re
dictw, err = {}, 0
for i in range(int(input())):
    s = input()
    dictw.setdefault(s.lower(), set()).add(s)
for word in input().split():
    if len(re.findall(r'[A-Z]', word)) != 1 or word.lower() in dictw and \
            word not in dictw[word.lower()]:  # sum(map(str.isupper, word)) подсчет БОЛЬШИХ букв
        err += 1
print(err)
