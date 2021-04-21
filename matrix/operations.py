from .matrices import ComplexMatrix, RealMatrix


class BasicMatrixOpsMixin:
    WRONG_OPERATION = "operacja niewykonalna"

    def sum(self, matrix):
        new_matrix = self.copy()

        if new_matrix.m != matrix.m or new_matrix.n != matrix.n:
            print(self.WRONG_OPERATION)
            return self.blank_copy()

        for i in range(new_matrix.m):
            for j in range(new_matrix.n):
                new_matrix.values[i][j] = new_matrix.values[i][j] + matrix.values[i][j]

        return new_matrix

    def mulmat(self, matrix):
        new_matrix = self.copy()

        if new_matrix.n != matrix.m:
            print(self.WRONG_OPERATION)
            return self.blank_copy()

        new_values = list()
        for row in range(new_matrix.m):  # wiersze
            new_values.append([])
            for column in range(matrix.n):  # kolumny
                sum = 0
                for i in range(new_matrix.n):
                    sum = sum + new_matrix.values[row][i] * matrix.values[i][column]

                new_values[row].append(sum)

        new_matrix.values = new_values
        new_matrix.n = matrix.n
        return new_matrix

    def mulsca(self, scalar):
        new_matrix = self.copy()

        for i in range(new_matrix.m):
            for j in range(new_matrix.n):
                new_matrix.values[i][j] = new_matrix.values[i][j] * scalar

        return new_matrix

    def tran(self):
        new_matrix = self.copy()
        new_values = list()
        for i in range(new_matrix.n):
            new_values.append([])

        for row in range(new_matrix.m):
            for i in range(new_matrix.n):
                new_values[i].append(new_matrix.values[row][i])

        [new_matrix.m, new_matrix.n, new_matrix.values] = [new_matrix.n, new_matrix.m, new_values]

        return new_matrix


class BasicComplexMatrixOpsMixin:
    def herm(self):
        new_matrix = self.copy()
        new_values = list()
        for i in range(new_matrix.n):
            new_values.append([])

        for row in range(new_matrix.m):
            for i in range(new_matrix.n):
                # i cannot use numpy.conj
                conjugate = complex(new_matrix.values[row][i].real, -new_matrix.values[row][i].imag)
                new_values[i].append(conjugate)

        [new_matrix.m, new_matrix.n, new_matrix.values] = [new_matrix.n, new_matrix.m, new_values]

        return new_matrix


class MatrixWithOps(BasicMatrixOpsMixin, RealMatrix): pass
class ComplexMatrixWithOps(BasicMatrixOpsMixin, BasicComplexMatrixOpsMixin, ComplexMatrix): pass


class ReducedRowEchelonForm(MatrixWithOps):
    def __replace_row(self, index1, index2):
        first_row = self.values[index1][:]
        self.values[index1] = self.values[index2][:]
        self.values[index2] = first_row

        return self

    def __find_not_zero_cell(self, offset_rows, offset_columns):
        for x in range(offset_columns, self.n):
            for y in range(offset_rows, self.m):
                if self.values[y][x] != 0:
                    return y, x

        return None, None

    def print_rank(self):  # rząd
        rank = 0
        for row in range(self.m):
            if any(cell != 0 for cell in self.values[row]):
                rank = rank + 1
        print(rank)

        return self

    def make(self):
        new_matrix = self.copy()
        offset_rows = 0
        offset_columns = 0

        for _ in range(new_matrix.m):
            y, x = new_matrix.__find_not_zero_cell(offset_rows, offset_columns)
            if y is None and x is None:
                break

            new_matrix.__replace_row(y, offset_rows)
            y = offset_rows

            divide_by = new_matrix.values[y][x]
            for i in range(offset_columns, new_matrix.n):
                new_matrix.values[y][i] = new_matrix.values[y][i] / divide_by

            for row in range(new_matrix.m):
                if row != y:
                    multiplier = new_matrix.values[row][x]
                    for i in range(offset_columns, new_matrix.n):
                        new_matrix.values[row][i] = new_matrix.values[row][i] - new_matrix.values[y][i] * multiplier

            offset_rows = y + 1
            offset_columns = x + 1

        return new_matrix


class TriangularMatrixOpsMixin:
    def get_values_on_diagonal(self):
        return [self.values[x][y] for x in range(self.n) for y in range(self.m) if x == y]

    def get_values_under_diagonal(self):
        return [self.values[x][y] for x in range(self.n) for y in range(self.m) if y < x]

    def get_values_above_diagonal(self):
        return [self.values[x][y] for x in range(self.n) for y in range(self.m) if y > x]

    def can_be_inverted(self):
        return all(value != 0 for value in self.get_values_on_diagonal())

    def get_filled_with_zeros_except_diagonal(self):
        new_matrix = self.copy()
        for x in range(new_matrix.n):
            for y in range(new_matrix.m):
                if x != y:
                    new_matrix.values[y][x] = 0
        return new_matrix


class TriangularMatrix(TriangularMatrixOpsMixin, MatrixWithOps):
    CANNOT_BE_INVERTED = "macierz nieodwracalna"

    def __invert_diagonal_matrix(self):
        new_matrix = self.copy()
        for i in range(new_matrix.n):
            new_matrix.values[i][i] = 1.0 / new_matrix.values[i][i]
        return new_matrix

    def __invert_lower_with_diagonal_filled_with_ones(self):
        opposite_matrix = self.copy().mulsca(-1)
        matrices_to_multiply = list()
        for column in range(self.n - 1):
            matrix = self.get_filled_with_zeros_except_diagonal()
            # wypelnij diagonalna jedynkami
            for x in range(matrix.n):
                for y in range(matrix.m):
                    if x == y:
                        matrix.values[y][x] = 1

            for i in range(self.m):
                if i != column:
                    matrix.values[i][column] = opposite_matrix.values[i][column]

            matrices_to_multiply.append(matrix)

        while len(matrices_to_multiply) > 1:
            a = matrices_to_multiply.pop()
            b = matrices_to_multiply.pop()
            matrices_to_multiply.append(
                a.mulmat(b)
            )

        return matrices_to_multiply[0]

    def __invert_lower(self):
        is_diagonal_filled_with_ones = all(value == 1 for value in self.get_values_on_diagonal())
        if is_diagonal_filled_with_ones:
            return self.__invert_lower_with_diagonal_filled_with_ones()

        D = self.get_filled_with_zeros_except_diagonal()
        for x in range(D.n):
            for y in range(D.m):
                if x == y:
                    D.values[y][x] = self.values[y][x]

        inverted_D = self.get_filled_with_zeros_except_diagonal()
        for x in range(D.n):
            for y in range(D.m):
                if x == y:
                    inverted_D.values[y][x] = 1.0 / D.values[y][x]

        A = self.copy()

        # L ma diagonalna wypelniona jedynkami
        L = inverted_D.mulmat(A)
        inverted_L = L.__invert_lower_with_diagonal_filled_with_ones()
        new_matrix = inverted_L.mulmat(inverted_D)
        return new_matrix

    def __invert_upper(self):
        lower = self.tran()
        inverted_lower = lower.__invert_lower()
        inverted_upper = inverted_lower.tran()
        return inverted_upper

    def invert(self):
        if not self.can_be_inverted():
            print(self.CANNOT_BE_INVERTED)
            return self.blank_copy()

        is_upper_filled_with_zeros = all(value == 0 for value in self.get_values_above_diagonal())
        is_lower_filled_with_zeros = all(value == 0 for value in self.get_values_under_diagonal())

        if is_upper_filled_with_zeros and is_lower_filled_with_zeros:
            return self.__invert_diagonal_matrix()

        elif is_upper_filled_with_zeros and not is_lower_filled_with_zeros:
            return self.__invert_lower()

        elif not is_upper_filled_with_zeros and is_lower_filled_with_zeros:
            return self.__invert_upper()

