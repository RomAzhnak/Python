wcount = {}
allv = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        wcount[' '.join(line[:-1])] = (int(line[-1]), 0)
allv = sum(x[0] for x in wcount.values()) / 450
for elem in wcount:
    wcount[elem] = (int(wcount[elem][0] // allv), wcount[elem][0] % allv)
balance = 450 - sum(wcount.get(x)[0] for x in wcount)
wc = sorted(wcount.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)
for i in range(balance):
    wcount[wc[i][0]] = wc[i][1][0]+1, wc[i][1][1]
# print(*[i + ' ' + str(wcount[i][0]) for i in wcount], sep='\n')
[print(key, wcount[key][0]) for key in wcount]

# второй вариант
p_dict, p_list, quotient, seats = dict(), list(), 0, 450
with open('input.txt', encoding='utf8') as inf:
    for idx, line in enumerate(inf):
        s = line.strip().split()
        p_dict[idx] = [' '.join(s[:-1]), int(s[-1])]
        quotient += int(s[-1])
quotient /= seats
for key, val in p_dict.items():
    p_dict[key].append(int(val[1] / quotient))
    p_list.append([val[1] / quotient % 1, val[1], key])
    seats -= int(val[1] / quotient)
for part in sorted(p_list, reverse=True):
    if seats:
        p_dict[part[2]][2] += 1
        seats -= 1
[print(p_dict[key][0], p_dict[key][2]) for key in sorted(p_dict)]