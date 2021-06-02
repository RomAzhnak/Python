def isPointInArea(x, y):
    return 2 <= ((x + 1)**2 + (y - 1)**2)**0.5 and x <= -y\
           and x >= (y - 2) / 2 or 2 >= ((x + 1)**2 + (y - 1)**2)**0.5 \
           and x >= -y and x <= (y - 2) / 2


x, y = float(input()), float(input())
if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
