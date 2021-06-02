n = int(input())
x = float(input())
a = float(input())
i = 1
p = a * x
while i < n:
    a = float(input())
    p = (p + a) * x
    i += 1
a = float(input())
p = p + a
print(round(p, 2))
