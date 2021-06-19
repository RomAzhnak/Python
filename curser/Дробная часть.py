x = float(input())
n = 0
while (x * 10**n) % 1 != 0:
    n += 1
g = str('{0:.') + str(n) + 'f}'
z = x - int(x)
print(g.format(z))