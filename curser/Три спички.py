l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
if l2 - r3 > 0 or l3 - r2 > 0:                                     # не пересек 2 и 3
    if (l1 - r2) * (l2 - r1) >= 0 and (l1 - r3) * (l3 - r1) >= 0:  # 1 2 3 пересек
        print(0)
    elif (l3 - r2 > 0) and (l3 - r2 <= r1 - l1):
        print(1)
    elif (l2 - r3 > 0) and (l2 - r3 <= r1 - l1):
        print(1)
    elif (l3 - r1 > 0) and (l3 - r1 <= r2 - l2):
        print(2)
    elif (l1 - r3 > 0) and (l1 - r3 <= r2 - l2):
        print(2)
    elif (l3 - r1 <= 0) and (l1 - r3 <= 0):
        print(2)
    elif (l1 - r2 > 0) and (l1 - r2 <= r3 - l3):
        print(3)
    elif (l2 - r1 > 0) and (l2 - r1 <= r3 - l3):
        print(3)
    elif (l2 - r1 <= 0) and (l1 - r2 <= 0):
        print(3)
    else:
        print(-1)
else:                           # пересек 2 и 3
    if l2 > l3:
        l2 = l3
    if r3 > r2:
        r2 = r3
    if l1 - r2 > 0 or l2 - r1 > 0:
        print(1)
    else:
        print(0)
