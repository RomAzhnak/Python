def IsPointInCircle(x, y, xc, yc, r):
    return r >= ((x - xc)**2 + (y - yc)**2)**0.5


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
