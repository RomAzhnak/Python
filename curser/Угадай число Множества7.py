with open('input.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    numset = set([str(i) for i in range(1, n + 1)])
    tmpline = f.readline().strip()
    while tmpline != "HELP":
        tmpline = set(tmpline.split())
        tmpstr = f.readline().strip()
        if tmpstr == "NO":
            numset -= tmpline
        else:
            numset &= tmpline
        tmpline = f.readline().strip()

print(*sorted(map(int, numset)))
