from itertools import accumulate
from operator import mul
from math import factorial
print(*accumulate([1]+list(range(1, int(input())+1)), mul))
print(*map(lambda x: factorial(x), range(int(input()) + 1)))
