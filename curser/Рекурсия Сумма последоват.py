def summ():
    n = int(input())
    if n == 0:
        return 0
    return n + summ()


print(summ())
