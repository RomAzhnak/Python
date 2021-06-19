p, x, y = int(input()), int(input()), int(input())
val = x * 100 + y
val = int(val + val * p / 100)
print(val // 100, val % 100)
