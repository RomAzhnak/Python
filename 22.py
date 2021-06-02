a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
n = d * a - b * c
if a == b == c == d == e == f == 0:
    print(5)
elif b == d == 0 and a != 0 and c * e / a == f:
    print(3, e / a)
elif b == d == 0 and c != 0 and a * f / c == e:
    print(3, f / c)
elif a == c == 0 and b != 0 and d * e / b == f:
    print(4, e / b)
elif a == c == 0 and d != 0 and b * f / d == e:
    print(4, f / d)
elif c * d != 0 and e == 0 and a / c == b / d and (f == 0 or a == b == e):
    print(1, -c / d, f / d)
elif a * b != 0 and f == 0 and c / a == d / b and (e == 0 or c == d == f):
    print(1, -a / b, e / b)
elif n != 0:
    print(2, (d * e - f * b) / n, (f * a - e * c) / n)
elif a * b * e * c * d * f != 0 and a / c == b / d == e / f:
    print(1, -a / b, e / b)
else:
    print(0)
