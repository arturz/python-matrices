from .matrices import ComplexMatrix


class BasicOperations(ComplexMatrix):
    WRONG_OPERATION = "operacja niewykonalna"

    def sum(self, matrix):
        if self.m != matrix.m or self.n != matrix.n:
            print(self.WRONG_OPERATION)
            return ComplexMatrix()

        for i in range(self.m):
            for j in range(self.n):
                self.values[i][j] = self.values[i][j] + matrix.values[i][j]

        return self

    def mulmat(self, matrix):
        if self.n != matrix.m:
            print(self.WRONG_OPERATION)
            return ComplexMatrix()

        new_values = list()
        for row in range(self.m):  # wiersze
            new_values.append([])
            for column in range(matrix.n):  # kolumny
                sum = 0
                for i in range(self.n):
                    sum = sum + self.values[row][i] * matrix.values[i][column]

                new_values[row].append(sum)

        self.values = new_values
        self.n = matrix.n
        return self

    def mulsca(self, scalar):
        for i in range(self.m):
            for j in range(self.n):
                self.values[i][j] = self.values[i][j] * scalar

        return self

    def tran(self):
        new_values = list()
        for i in range(self.n):
            new_values.append([])

        for row in range(self.m):
            for i in range(self.n):
                new_values[i].append(self.values[row][i])

        self.values = new_values
        [self.m, self.n] = [self.n, self.m]

        return self

    def herm(self):
        new_values = list()
        for i in range(self.n):
            new_values.append([])

        for row in range(self.m):
            for i in range(self.n):
                # i cannot use numpy.conj
                conjugate = complex(self.values[row][i].real, -self.values[row][i].imag)
                new_values[i].append(conjugate)

        self.values = new_values
        [self.m, self.n] = [self.n, self.m]

        return self
