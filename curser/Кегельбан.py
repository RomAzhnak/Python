n, k = map(int, input().split())
lst = ['I' for _ in range(n)]
for i in range(k):
    l, r = map(int, input().split())
    lst[l - 1: r] = '.' * (r - l + 1)
print(*lst, sep='')
