from operator import attrgetter, itemgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs


print(multisort(list(student_objects), (('grade', True), ('age', False))))
print(sorted(student_tuples, key=itemgetter(2), reverse=True))\

s = [4, 5, 8, 2, 3, 1, 9, 0, 5, 4, 2, 1]
s = sorted(s)[-1]       # максимальный элемент в списке
print(s)

decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
print([student for grade, i, student in decorated])
print(*decorated)
