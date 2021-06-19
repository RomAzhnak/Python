n = int(input())
s = ''
for i in range(1, n+1):
    s = ''.join(str(j) for j in range(1, i + 1))
    print(s)
# или
    s = tuple(range(1, i + 1))
    print(*s, sep='')

# второй вариант
# n = int(input())
for i in range(1, n+1):
    print(*list(range(1, i+1)), sep='')
