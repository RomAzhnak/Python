def lagrange(n, i):
    sqr = int(n**0.5)
    if n - sqr**2 == 0:
        return str(sqr)
    if i == 1:
        return 0
    while lagrange(n - sqr**2, i - 1) == 0:
        sqr -= 1
        if sqr == 0:
            return 0
    return str(sqr) + ' ' + lagrange(n - sqr**2, i - 1)


n = int(input())
print(lagrange(n, 4))
