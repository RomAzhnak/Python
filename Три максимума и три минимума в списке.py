from random import randint
lst = [randint(-10, 10) for _ in range(10)]
print(*lst)
# lst = list(map(int, input().split()))
mini, maxi = [lst[0], lst[1], lst[2]], [lst[0], lst[1], lst[2]]
maxi.sort(reverse=True)
mini.sort()
for i in range(3, len(lst)):
    if mini[2] >= lst[i]:
        mini[2] = lst[i]
        mini.sort()
    if lst[i] >= maxi[2]:
        maxi[2] = lst[i]
        maxi.sort(reverse=True)
print(*mini, '   ', *maxi)
if mini[0] * mini[1] * maxi[0] > maxi[0] * maxi[1] * maxi[2]:
    print(mini[0], mini[1], maxi[0])
else:
    print(*maxi)
# Второй способ
# from random import randint
randList = [randint(-10, 10) for _ in range(10)]
print(*randList)
a = b = c = float('-inf')
for el in randList:
    if el > a:
        a, b, c = el, a, b
    elif el > b:
        b, c = el, b
    elif el > c:
        c = el

# print(randList)
print('{}, {}, {}'.format(a, b, c))
"""
a = list(map(int, input().split()))
j = len(a)
max1, imax1 = a[0], 0
max2, imax2 = a[j - 1], j - 1
max3, imax3 = -1000000 - 1, 0
min1, imin1 = a[0], 0
min2, imin2 = a[j - 1], j - 1
min3, imin3 = 1000000 + 1, 0
for i in range(j):
    if max1 < a[i] and i != imax2:
        max3 = max1
        max1, imax1 = a[i], i
    if max2 < a[j - i - 1] and j - i - 1 != imax1 and j - i - 1 != imax3:
        max2, imax2 = a[j - i - 1], j - i - 1
    if max3 < a[i] and i != imax1 and i != imax2:
        max3, imax3 = a[i], i
    if min1 > a[i] and i != imin2:
        min3 = min1
        min1, imin1 = a[i], i
    if min2 > a[j - i - 1] and j - i - 1 != imin1 and j - i - 1 != imin3:
        min2, imin2 = a[j - i - 1], j - i - 1
    if min3 > a[i] and i != imin1 and i != imin2:
        min3, imin3 = a[i], i
min1 = sorted([min1, min2, min3])
max1 = sorted([max1, max2, max3])
if min1[0] * min1[1] * max1[2] > max1[0] * max1[1] * max1[2]:
    print(min1[0], min1[1], max1[2])
else:
    print(max1[0], max1[1], max1[2])
"""