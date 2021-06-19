def sqware():
    global i
    n = int(input())
    if n == 0:
        return
    sqware()
    if n - int(n**0.5)**2 == 0:
        i = 1
        print(int(n**0.5)**2, end=' ')


i = 0
sqware()
if i == 0:
    print(0)

""" второй вариант
def sqware(i):
    n = int(input())
    if n == 0:
        return 0
    i = sqware(i)
    sqw = int(n**0.5)
    if n - sqw**2 == 0:
        i = 1
        print(sqw**2, end=' ')
    return i


if sqware(0) == 0:
    print(0)"""