from sys import stdin
import copy


class Matrix:
    def __init__(self, dim):
        self.dim = [line[:] for line in dim]    # self.dim = copy.deepcopy(dim)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.dim])

    def size(self):
        return len(self.dim), len(self.dim[0])


exec(stdin.read())
