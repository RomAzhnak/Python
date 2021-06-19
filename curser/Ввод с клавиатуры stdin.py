from sys import stdin

#for line in stdin:
#    print(line.rstrip('\n')[::-1])

#print([line.rstrip('\n')[::-1] for line in stdin]) # выдает список с ответами в конце
[print(line.rstrip('\n')[::-1]) for line in stdin]  # выдает ответ сразу построчно(генератор)
"""
import sys

r = []
for i in range(int(sys.stdin.readline())):  # количество строк
    s = sys.stdin.readline()
    count = int(s.split(' ', 1)[0])
    r.append((count, str(i + 1)))

print(r)
r.sort()
print(r)

sys.stdout.write(' '.join(i for _, i in r))
"""