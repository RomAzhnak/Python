n = int(input())
x = float(input())
p = float(input())
while n != 0:
    a = float(input())
    p = p * x + a
    n -= 1
print("{0:.2f}".format(p))
