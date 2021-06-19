def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)


a, b = int(input()), int(input())
print(sum(a, b))
