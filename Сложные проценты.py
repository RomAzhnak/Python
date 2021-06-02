p, x, y, k = int(input()), int(input()), int(input()), int(input())
val = x * 100 + y
i = 1
while i <= k:
    val = int(val + val * p / 100)
    i += 1
print(val // 100, val % 100)
