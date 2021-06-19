from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, d):
        self.dim = [line[:] for line in d]

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
                                for j in range(len(self.dim[i]))])  # Matrix(list(map(lambda a, b: list(map(lambda x, y: x + y, a, b)), self.dim, other.dim)))
                else:
                    raise MatrixError(self, other)
            return Matrix(mas)
        else:
            raise MatrixError(self, other)

    def mulmatrix(self, other):
        mas = [[0 for i in range(len(other.dim))]
               for j in range(len(self.dim))]
        for i in range(len(self.dim)):
            for j in range(len(other.dim)):
                if len(self.dim[i]) == len(other.dim[j]):
                    mas[i][j] = Matrix.mulvec(self.dim[i], other.dim[j])
                else:
                    tmp = Matrix.transposed(other)
                    raise MatrixError(self, tmp)
        return Matrix(mas)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            mas = [list(map(lambda x: x * other, y)) for y in self.dim]
#            mas = []
#            for i in range(len(self.dim)):
#                mas.append([self.dim[i][j] * other
#                            for j in range(len(self.dim[i]))])
            return Matrix(mas)
        elif isinstance(other, Matrix):
            tmp = Matrix.transposed(other)
            tmp = Matrix.mulmatrix(self, tmp)
            return tmp
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        self.dim = list(zip(*self.dim))
        return Matrix(self.dim)

    @staticmethod
    def mulvec(vec1, vec2):
        return sum([i * j for i, j in zip(vec1, vec2)])

    @staticmethod
    def transposed(d):
        return Matrix(list(zip(*d.dim)))


exec(stdin.read())
