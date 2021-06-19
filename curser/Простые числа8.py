from math import sqrt
print(*filter(lambda x: x % 2 != 0 and all(map(lambda i: x % i != 0, range(3, int(sqrt(x)) + 1, 2))) or x == 2,
              range(2, int(input()) + 1)))
# вместо x % 2 != 0 и x % i != 0 можно писать x % 2 и x % i

# второй вариант
print(*filter(lambda x: x % 2 != 0 and all(x % y != 0 for y in range(3, round(sqrt(x)) + 1, 2)) or x == 2,
              range(2, int(input()) + 1)))
