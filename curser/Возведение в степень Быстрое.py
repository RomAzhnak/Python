import time


def fastexp(b, n):
    a = 1
    while n != 1:
        if n % 2 == 1:
            a *= b
            n -= 1
        b *= b
        n //= 2
    b *= a
    return b


def exp(x, a):
    n = bin(a)[2:]
    x_n = 1
    for i in n:
        if int(i) == 0:
            x_n = x_n**2
        else:
            x_n = x*(x_n**2)
    return x_n


def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


ex = 5
start = time.time()
print(fastexp(11, ex))
end = time.time()
print(end - start)
start = time.time()
exp(11, ex)
end = time.time()
print(end - start)
start = time.time()
fast_pow(11, ex)
end = time.time()
print(end - start)
start = time.time()
pow(11, ex)
end = time.time()
print(end - start)
