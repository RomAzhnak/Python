x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
dx = x2 - x1
dy = y2 - y1
d = (x1 + y1) % 2 + (x2 + y2) % 2
if dx < 0:
    dx = -dx
if d == 0 and dy >= dx:
    print('YES')
else:
    print('NO')
