import string
with open('input.txt', 'r', encoding='utf-8') as f:
    t = tuple(map(lambda s: s.rstrip().rstrip(string.punctuation), f.readlines()))
    f.seek(0)
    a = f.read().split()
a = {s.rstrip(string.punctuation) for s in a}
a = {s.lower() for s in a}
print(t)
print(a)
