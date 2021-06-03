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
                                for j in range(len(self.dim[i]))])
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

    def solve(self, vector):
        if self.size()[0] != self.size()[1]:
            raise Exception("Matrix not square!")
        elif self.size()[1] != len(vector):
            raise Exception("Matrix and vector different length!")
        masd = []
        for i in range(len(vector)):
            mas = Matrix(self.dim)
            for j in range(len(vector)):
                mas.dim[j][i] = vector[j]
            masd.append(Matrix.determinator(mas))
        return list(map(lambda x: x / Matrix.determinator(self), masd))

    @staticmethod
    def mulvec(vec1, vec2):
        return sum([i * j for i, j in zip(vec1, vec2)])

    @staticmethod
    def transposed(d):
        return Matrix(list(zip(*d.dim)))

    @staticmethod
    def determinator(m):
        if m.size()[0] == 2:
            return m.dim[0][0] * m.dim[1][1] - m.dim[0][1] * m.dim[1][0]
        elif m.size()[0] == 3:
            return \
                m.dim[0][0] * m.dim[1][1] * m.dim[2][2] \
                + m.dim[2][0] * m.dim[0][1] * m.dim[1][2] \
                + m.dim[1][0] * m.dim[2][1] * m.dim[0][2] \
                - m.dim[2][0] * m.dim[1][1] * m.dim[0][2] \
                - m.dim[0][0] * m.dim[2][1] * m.dim[1][2] \
                - m.dim[1][0] * m.dim[0][1] * m.dim[2][2]
        else:
            raise Exception("Matrix range more than 3")


class SquareMatrix(Matrix):
    def q__pow__(self, power, modulo=None):  # def exp(x, a):
        if power < 2:
            return self
        n = bin(power)[2:]
        x_n = 1
        for i in n:
            if int(i) == 0:
                x_n = x_n * x_n
            else:
                x_n = self * (x_n * x_n)
        return x_n

    def __pow__(self, p, modulo=None):
        if p in [0, 1]:
            return self
        elif p == 2:
            return self * self
        if p % 2 != 0:
            return self * (self ** (p - 1))
        else:
            return (self * self) ** (p // 2)


exec(stdin.read())
