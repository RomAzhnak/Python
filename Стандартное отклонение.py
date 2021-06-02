n = 0
x = int(input())
z = 0
z1 = 0
while x != 0:
    n += 1
    z += x**2
    z1 += x
    x = int(input())
res = ((z - z1**2 / n) / (n - 1))**0.5
print(res)
