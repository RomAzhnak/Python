a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
dd = a * d - b * c
dx = d * e - b * f
dy = a * f - c * e
if dd != 0:
    print('2', dx / dd, dy / dd)
elif a == b == c == d == e == f == 0:
    print(5)
elif a == b == 0 and e != 0 or c == d == 0 and f != 0:
    print(0)
elif dd == 0:
    if dx != 0 or dy != 0:
        print(0)
    else:
        if b == d == 0 and a != c:
            print(3, (e - f) / (a - c))
        elif b == d == 0 and a == c:
            print(3, e / a)
        elif a == c == 0 and b != d:
            print(4, (e - f) / (b - d))
        elif a == c == 0 and b == d:
            print(4, e / b)
        elif c == d == 0:
            print(1, -a / b, e / b)
        else:
            print(1, -c / d, f / d)
