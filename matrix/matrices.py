from fractions import Fraction
from copy import deepcopy


class ComplexMatrix(object):
    def __init__(self, m=0, n=0):
        self.m = m  # wiersze
        self.n = n  # kolumny
        self.values = list()

        for i in range(self.m):
            self.values.append([None for _ in range(self.n)])

    @staticmethod
    def prompt_row_values():
        return list(map(complex, input().split()))

    def prompt_values(self):
        values = list()
        sizes = list(map(int, input().split()))

        # macierz kwadratowa
        if len(sizes) == 1:
            m = sizes[0]
            n = sizes[0]
        else:
            m, n = sizes

        for i in range(m):
            values.append(self.prompt_row_values())

        self.values = values
        self.m = m
        self.n = n

        return self

    def print_values(self):
        for i in range(self.m):
            print(" ".join(list(map(str, self.values[i]))))

        return self

    def copy(self):
        return deepcopy(self)

    def blank_copy(self):
        copy = self.copy()
        [copy.values, copy.m, copy.n] = [list(), 0, 0]
        return copy


class RealMatrix(ComplexMatrix):
    @staticmethod
    def prompt_row_values():
        return [float(Fraction(value)) for value in input().split()]

    def print_values(self):
        def round_if_needed(number):
            if round(number, 1) != round(number, 10):
                return "%.2f" % round(number, 2)
            return "%.1f" % number

        for i in range(self.m):
            print(" ".join([str(round_if_needed(number + 0)) for number in self.values[i]]))

        return self
