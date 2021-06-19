# from sys import stdin
# from functools import reduce
# print(['True', 'False'][next(filter(lambda x: x == 0, map(int, stdin.read().split())), 1)])

# второй вариант
# print(reduce(lambda x, y: x * y, map(lambda x: int(input()), range(int(input())))) == 0)
# третий вариант
# print((any(list(map(lambda x: int(input()) == 0, range(int(input())))))))
print('0' in [str(input()) for i in range(int(input()))])
