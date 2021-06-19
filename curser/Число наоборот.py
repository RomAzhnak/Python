n = int(input())
i = 0
y = 0

while n % 10 > 0 or n > 9:
    y = y * 10 + n % 10
    n = n // 10
print(y)
