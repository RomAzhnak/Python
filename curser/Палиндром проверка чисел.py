a, b = int(input()), int(input())
for i in range(a, b + 1):
    if str(i)[::-1] == str(i):
        print(i)
