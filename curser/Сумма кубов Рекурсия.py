def lagrange(n, i):
    sqr = int(n**(1/3))
    if n - sqr**3 == 0:
        return str(sqr**3)
    if i == 1:
        return 0
    while lagrange(n - sqr**3, i - 1) == 0:
        sqr -= 1
        if sqr == 0:
            return 0
    return str(sqr**3) + ' ' + lagrange(n - sqr**3, i - 1)


n = int(input())
print(lagrange(n, 7))
