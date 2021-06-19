n = int(input())
j = 0
for i in range(n):
    j += int(input()) == 0
print(j)

# второй вариант
print([int(input()) for _ in range(int(input()))].count(0))

# третий вариант
print(sum(int(input()) == 0 for _ in range(int(input()))))
