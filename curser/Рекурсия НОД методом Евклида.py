def gcd(a, b):
    if a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        return gcd(a, b)
    else:
        return a + b


a, b = int(input()), int(input())
print(gcd(a, b))

"""def gcd(a, b):
    if b == 0: # Этот случай в тестах не учтён, но он должен быть, иначе ошибка деления на 0 при b=0
        return a
    elif a % b == 0:
        return b
    return gcd(b, a % b)


c = int(input())
d = int(input())
print(gcd(c, d))"""
