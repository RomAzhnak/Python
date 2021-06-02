lst = list(map(int, input().split()))
j = 0
for i in range(len(lst)):
    if lst[i - j] == 0:
        lst.pop(i - j)
        lst.append(0)
        j += 1
print(*lst)

# второй вариант Идем с конца
lst = (list(map(int, input().split())))
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 0:
        lst.append(lst.pop(i))
print(*lst)
