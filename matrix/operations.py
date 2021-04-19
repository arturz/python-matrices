from .matrices import ComplexMatrix, RealMatrix


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


class ReducedRowEchelonForm(RealMatrix):
    def find_not_zero_cell(self, offset_rows, offset_columns):
        for x in range(offset_columns, self.n):
            for y in range(offset_rows, self.m):
                if self.values[y][x] != 0:
                    return y, x

        return None, None

    def make(self):
        offset_rows = 0
        offset_columns = 0

        for _ in range(self.m):
            y, x = self.find_not_zero_cell(offset_rows, offset_columns)
            if y is None and x is None:
                break

            self.replace_row(y, offset_rows)
            y = offset_rows

            divide_by = self.values[y][x]
            for i in range(offset_columns, self.n):
                self.values[y][i] = self.values[y][i] / divide_by

            for row in range(self.m):
                if row != y:
                    multiplier = self.values[row][x]
                    for i in range(offset_columns, self.n):
                        self.values[row][i] = self.values[row][i] - self.values[y][i] * multiplier

            offset_rows = y + 1
            offset_columns = x + 1

        return self

    def print_rank(self):  # rząd
        rank = 0
        for row in range(self.m):
            if any(cell != 0 for cell in self.values[row]):
                rank = rank + 1
        print(rank)

        return self

