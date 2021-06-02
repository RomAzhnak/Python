n = int(input())
prev = 0
y = 1
i = 1
while n != 0:
    if n == prev:
        i += 1
    elif y < i:
        y = i
        i = 1
    else:
        i = 1
    prev = n
    n = int(input())
if y < i:
    y = i
print(y)
