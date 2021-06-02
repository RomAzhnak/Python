n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
n = n - 3
for i in a:
    if i - n > 2:
        count += 1
        n = i
print(count)
