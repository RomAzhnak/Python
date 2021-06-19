from itertools import accumulate

print(*list(accumulate(map(int, input().split()))))
