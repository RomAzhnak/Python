a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))**0.5
if s - int(s) == 0:
    print(int(s))
else:
    print('{0:.6f}'.format(s))
