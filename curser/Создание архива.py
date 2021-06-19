s, n = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
i = 0
count = 0
while s > 0 and i < len(a):
    if s - a[i] >= 0:
        count += 1
    s -= a[i]
    i += 1
print(count)
