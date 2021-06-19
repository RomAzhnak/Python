from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, d):
        self.dim = [line[:] for line in d]    # self.dim = copy.deepcopy(dim) или [_.copy() for _ in d]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.dim])

    def size(self):
        return len(self.dim), len(self.dim[0])

    def __add__(self, other):
        if len(self.dim) == len(other.dim):
            mas = []
            for i in range(len(self.dim)):
                if len(self.dim[i]) == len(other.dim[i]):
                    mas.append([self.dim[i][j] + other.dim[i][j]
                                for j in range(len(self.dim[i]))])
                else:
                    raise MatrixError(self, other)
            return Matrix(mas)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        mas = []
        for i in range(len(self.dim)):
            mas.append([self.dim[i][j] * other
                        for j in range(len(self.dim[i]))])
        return Matrix(mas)

    __rmul__ = __mul__

    def transpose(self):
        self.dim = list(zip(*self.dim))
        return Matrix(self.dim)

    @staticmethod
    def transposed(m1):
        return Matrix(list(zip(*m1.dim)))


exec(stdin.read())
