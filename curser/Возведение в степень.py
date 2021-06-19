def power(a, n):
    result = 1
    if n != 0:
        for i in range(1, n + 1):
            result *= a
    return result


a, n = float(input()), int(input())
if n < 0:
    if n % 2 == 0:
        res = 1 / power(a, -int(n / 2))
        res *= res
    else:
        res = 1 / power(a, -n // 2)
        res = res * res / a
else:
    if n % 2 == 0:
        res = power(a, int(n / 2))
        res *= res
    else:
        res = power(a, n // 2)
        res = res * res * a
print(res)
