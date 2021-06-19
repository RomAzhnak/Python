from operator import xor
print(*map(xor, map(int, input().split()), map(int, input().split())))
print(*map(lambda x, y: x ^ y, map(int, input().split()), map(int, input().split())))
