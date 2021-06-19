def phib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


a = int(input())
print(phib(a))


# второй вариант
print(list(map(lambda x, f=lambda x, f: (f(x-1, f)+f(x-2, f)) if x > 1 else 1:
               f(x, f), range(10))))
