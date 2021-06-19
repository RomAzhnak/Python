import itertools, operator


def unique_justseen(iterable, key=None):
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return map(operator.itemgetter(0), itertools.groupby(iterable, key))


#z = unique_justseen('AAAABBBCCDAABBB')
q = set()
#q = set(map(operator.itemgetter(0), itertools.groupby('AAAABBBCCDAABBB')))
#print(q)
#[print(x, list(y)) for x, y in itertools.groupby('AAAABBBCCDAABBB')]
seen = set()
iterable = 'AAAABBBCCDAABBBAAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSSSSSSSSSBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
[q.add(x) for x in itertools.filterfalse(lambda y: y in q, iterable)]
#[q.add(x) for x in filter(lambda x: x not in q, iterable)]
print(q)