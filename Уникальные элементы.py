lst = list(map(int, input().split()))
for now in lst:
    if lst.count(now) == 1:
        print(now, end=' ')
        
# второй вариант
print()
print(*[lst[i] for i in range(len(lst)) if lst.count(lst[i]) == 1])
