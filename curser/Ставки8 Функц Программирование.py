"""
Тест 1
Входные данные:
3 2
2 1 2 3
1 2 3 2
Вывод программы:
3 2 1

Тест 2
Входные данные:
3 4
1 2 1 3
1 2 3 1
1 2 2 3
1 2 3 2
Вывод программы:
0
"""

from itertools import permutations
from operator import indexOf
from sys import stdin
print(*next(
    map(
        lambda b:
        next(
            filter(
                lambda y:
                all(
                    map(
                        lambda x:
                        ((indexOf(y, x[0]) < indexOf(y, x[1])) ^
                         (indexOf(y, x[2]) < indexOf(y, x[3]))),
                        b[1])
                    ),
                b[0]),
            [0]),
        map(
            lambda a:
            [permutations(
                range(1, a + 1), a),
                list(
                    map(
                        lambda s:
                        tuple(map(int, s.split())), stdin.readlines()))],
            map(int, input().split()
                )
        )
    )
    )
      )
