n = int(input())
prev = n
count = 1
ch = 0
i = 1
while n != 0:
    if n < prev and ch <= 0:
        i += 1
        ch = -1
    elif n > prev and ch >= 0:
        i += 1
        ch = 1
    elif n == prev:
        ch = 0
        i = 1
    else:
        i = 2
        ch = -ch
    prev = n
    n = int(input())
    if count < i:
        count = i
print(count)
