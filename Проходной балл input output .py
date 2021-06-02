lst = []
with open('input.txt', 'r', encoding='utf-8') as f:
    k = int(f.readline())
    for line in f:
        tData = list(map(int, line.split()[-3:]))
        if tData[0] >= 40 and tData[1] >= 40 and tData[2] >= 40:
            lst.append(tData[0] + tData[1] + tData[2])
    if len(lst) <= k:
        ans = 0
    else:
        lst.sort(reverse=True)
        if lst[0] == lst[k]:
            ans = 1
        else:
            while lst[k-1] == lst[k]:
                k -= 1
            ans = lst[k-1]
    with open('output.txt', 'w', encoding='utf-8') as f:
        print(ans, file=f)
