from operator import xor
from functools import reduce
print(*reduce(lambda x, y: map(xor, x, y), map(lambda _: map(int, input().split()), range(int(input())))))

ls1, ls2, ls3 = [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]
print([ls1, ls2, ls3, ls1])
print(*reduce(lambda x, y: map(xor, x, y), (ls1, ls2, ls3, ls1)))
print(*map(lambda x: reduce(xor, x), list(zip(ls1, ls2, ls3, ls1))))    # тот же результ с поворотом матрицы на 90град

# поворачиваем матрицу на 90 градусов
print(list(zip(ls1, ls2, ls3, ls1)))
print(*reduce(lambda x, y: map(xor, x, y), zip(ls1, ls2, ls3, ls1)))
