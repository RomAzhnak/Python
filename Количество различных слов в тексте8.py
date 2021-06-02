from collections import Counter
from sys import stdin
print(
    len(
        Counter(
            open('input.txt', 'r', encoding='utf-8').read().split()
                )
        )
    )
print(len(Counter(stdin.read().split())))

"""# третий вариант
import sys

print(len(set(sys.stdin.read().split())))
"""