a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4 * a * c
if a == b == c == 0:
    print(3)
elif (a == 0 and b == 0) or d < 0:
    print(0)
elif a == 0:
    print('1', -c / b)
elif d == 0:
    print('1', -b / (2 * a))
elif d > 0:
    res1 = (-b + d**0.5) / (2 * a)
    res2 = (-b - d**0.5) / (2 * a)
    if res1 > res2:
        res1, res2 = res2, res1
    print('2', res1, res2)
