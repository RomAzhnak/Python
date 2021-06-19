def move(n, x, y):
    if n == 1:
        print(n, x, y)
        return
    move(n - 1, x, 6 - x - y)
    print(n, x, y)
    move(n - 1, 6 - x - y, y)


n = int(input())
move(n, 1, 3)
