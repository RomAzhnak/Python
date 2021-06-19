"""
Тест 1
Входные данные:
9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I

Вывод программы:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2

Тест 2
Входные данные:
10
AQHFYP MKFXCLZBT
AYKOTYQ QIUKGHWCDC
IWCGKHMFM WPLHJL
MJVAURUDN QIUKGHWCDC
MKFXCLZBT IWCGKHMFM
PUTRIPYHNQ UQNGAXNP
QIUKGHWCDC WPLHJL
UQNGAXNP WPLHJL
YURTPJNR QIUKGHWCDC

Вывод программы:
AQHFYP 3
AYKOTYQ 2
IWCGKHMFM 1
MJVAURUDN 2
MKFXCLZBT 2
PUTRIPYHNQ 2
QIUKGHWCDC 1
UQNGAXNP 1
WPLHJL 0
YURTPJNR 2

def familytree(dict_tree, people, depth=0):
    for p in people:
        lst.append([p, depth])
        if p not in dict_tree:
            people = []
        else:
            people = dict_tree[p]
        familytree(dict_tree, people, depth+1)


tree, set1, set2, lst = {}, set(), set(), []
for _ in range(int(input()) - 1):
    line = input().split()
    tree.setdefault(line[1], []).append(line[0])
    set1.add(line[1])
    set2.add(line[0])
set1 -= set2

familytree(tree, [first])
[print(x, y) for x, y in sorted(lst)]
"""


# второй вариант
def familytree1(person):
    if person not in tree:
        return 0
    else:
        return 1 + familytree1(tree[person])


tree = {}
for _ in range(int(input()) - 1):
    line = input().split()
    tree.setdefault(line[0], line[1])
for s in sorted(tree.keys() | tree.values()):
    print(s, familytree1(s))


# третий вариант
tree = dict()


def get_parent(child):
    return 0 if not len(tree[child]) else 1 + get_parent(tree[child])


with open('input.txt', encoding='utf8') as inf:
    _ = int(inf.readline())
    for line in inf:
        child, parent = line.strip().split()
        tree[child] = parent
        tree[parent] = tree.get(parent, '')  # для родоначальника
print(tree)
[print(child, get_parent(child)) for child in sorted(tree)]
