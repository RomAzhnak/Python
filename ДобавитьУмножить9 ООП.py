from sys import stdin


class Matrix:
    def __init__(self, dim):
        self.dim = [line[:] for line in dim]    # self.dim = copy.deepcopy(dim)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.dim])

    def size(self):
        return len(self.dim), len(self.dim[0])

    def __add__(self, other):
        mas = []
        for i in range(len(self.dim)):
            mas.append([self.dim[i][j] + other.dim[i][j]
                        for j in range(len(self.dim[i]))])
        return Matrix(mas)

    def __mul__(self, other):
        mas = []
        for i in range(len(self.dim)):
            mas.append([self.dim[i][j] * other
                        for j in range(len(self.dim[i]))])
        return Matrix(mas)

    __rmul__ = __mul__


exec(stdin.read())
