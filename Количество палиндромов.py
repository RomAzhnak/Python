k = int(input())
i = 1
y = 0
while i <= k:
    num = i
    n = 0
    while num % 10 > 0 or num > 9:
        n = n * 10 + num % 10
        num = num // 10
    if n == i:
        y += 1
    i += 1
print(y)
