class ComplexMatrix:
    values = list()
    m = 0  # wiersze
    n = 0  # kolumny

    @staticmethod
    def prompt_row_values():
        return list(map(complex, input().split(' ')))

    def prompt_values(self):
        values = list()
        m, n = list(map(int, input().split(' ')))

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


class RealMatrix(ComplexMatrix):
    @staticmethod
    def prompt_row_values():
        return list(map(int, input().split(' ')))