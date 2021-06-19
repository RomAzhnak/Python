def reduceFraction(n, m):
    p, q = n, m
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    return int(p / (n + m)), int(q / (n + m))


a, b = int(input()), int(input())
print(*reduceFraction(a, b))
