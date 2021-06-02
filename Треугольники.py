a = int(input())
b = int(input())
c = int(input())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if a >= b + c:
    print('impossible')
elif b**2 + c**2 == a**2:
    print('rectangular')
elif b**2 + c**2 > a**2:
    print('acute')
else:
    print('obtuse')
    