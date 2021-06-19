n = int(input())
s = 0
i = 1
while i <= n:
    s = s + 1 / i**2
    i += 1
if s - int(s) == 0:
    print(int(s))
elif n % 2 == 0:
    print(s)
else:
    print('{0:.5f}'.format(s))
