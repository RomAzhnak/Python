import itertools

print(min(itertools.filterfalse(lambda x: not(x % 2), map(int, input().split()))))
