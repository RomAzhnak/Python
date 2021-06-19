a, b, c = int(input()), int(input()), int(input())
x = 0
if a == b:
    x += 1
if a == c:
    x += 1
elif b == c:
    x += 1
x += 1
if x == 1:
    x = 0
print(x)
