a = list(map(int, input().split()))
j = len(a)
max1, imax1 = a[0], 0
max2, imax2 = a[j - 1], j - 1
min1, imin1 = a[0], 0
min2, imin2 = a[j - 1], j - 1
for i in range(j):
    if max1 < a[i] and i != imax2:
        max1, imax1 = a[i], i
    if max2 < a[j - i - 1] and j - i - 1 != imax1:
        max2, imax2 = a[j - i - 1], j - i - 1
    if min1 > a[i] and i != imin2:
        min1, imin1 = a[i], i
    if min2 > a[j - i - 1] and j - i - 1 != imin1:
        min2, imin2 = a[j - i - 1], j - i - 1
if min1 * min2 > max1 * max2:
    print(*sorted([min1, min2]))
else:
    print(*sorted([max1, max2]))
