x = float(input())
a = int((x - int(x)) * 100)
if a >= 50:
    x = x + 0.1
print(round(x))
