def c(n, k):
    if k == 1:
        return n
    elif n == k:
        return 1
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


n, k = int(input()), int(input())
if k == 0:
    print(1)
else:
    print(c(n, k))
