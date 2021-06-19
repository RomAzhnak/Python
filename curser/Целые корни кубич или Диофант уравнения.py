a, b, c, d, e = int(input()), int(input()), int(input()), int(input()),\
                int(input())
print([x for x in range(0, 1001) if x != e and (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0])
