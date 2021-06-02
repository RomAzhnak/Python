lst = list(map(int, input().split()))
maxi, maximum = 0, 0
for i in lst:
    if lst.count(i) > maxi:
        maxi = lst.count(i)
        maximum = i
print(maximum)
