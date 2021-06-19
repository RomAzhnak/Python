with open('input.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    numSet = set([str(i) for i in range(1, n + 1)])
    answer = []
    tmpLine = f.readline().strip()
    while tmpLine != "HELP":
        tmpLine = set(tmpLine.split())
        if len(tmpLine & numSet)*2 <= len(numSet):
            numSet -= tmpLine
            print("NO")
        else:
            numSet &= tmpLine
            print("YES")
        tmpLine = f.readline().strip()
print(*sorted(map(int, numSet)))
