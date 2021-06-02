from collections import defaultdict


def preprocess(family_list):
    descent_dict = defaultdict(list)
    for person in family_list:
        descent_dict[person["parent"]].append(person["name"])
    return descent_dict


def print_family_tree(descent_dict, people, depth=0):
    for person in people:
        print("  "*depth+person)
        print_family_tree(descent_dict, descent_dict[person], depth+1)


family = [
    {'name': 'a', 'parent': ''},
    {'name': 'b', 'parent': 'a'},
    {'name': 'c', 'parent': 'a'},
    {'name': 'd', 'parent': 'b'},
    {'name': 'e', 'parent': 'd'},
    {'name': 'f', 'parent': ''},
    {'name': 'g', 'parent': 'f'},
    {'name': 'h', 'parent': 'a'}
]
d = preprocess(family)
print(d)
print_family_tree(d, d[''])
