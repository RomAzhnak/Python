"""
from sys import stdin


def countsort(m, amount):
    tmarks = [0] * amount
    s = ''
    for mark in m:
        tmarks[mark] += 1
    for mark in range(amount):
        s += (str(mark)+' ')*tmarks[mark]
#    m.extend(map(int, s.split()))          # изменяет список из основной программы
    m[::] = list(map(int, s.split()))       # изменяет список из основной программы
#    m = s                                  # не изменяет список из основной программы


marks = list(map(int, stdin.readline().split()))
if marks:
    countsort(marks, max(marks)+1)
print(marks)
"""


# второй вариант с модификацией исходного списка
def countsort(a, amount):
    counts = [0 for _ in range(amount)]
    for i in a:
        counts[i] += 1
    a[::] = []
    print(counts)
    for i in range(amount):
        a.extend([i for _ in range(counts[i])])


a = list(map(int, input().split()))
countsort(a, max(a)+1)
print(*a)
