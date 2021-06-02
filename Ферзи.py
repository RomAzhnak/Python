x = [0] * 8
y = [0] * 8
res = False
for i in range(8):
    x[1], y[1] = map(int, input().split())
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or \
                (abs(x[i] - x[j]) == abs(y[i] - y[j])):
            res = True
print('YES') if res else print('NO')
