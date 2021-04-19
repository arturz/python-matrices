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

    def replace_row(self, index1, index2):
        first_row = self.values[index1][:]
        self.values[index1] = self.values[index2][:]
        self.values[index2] = first_row


class RealMatrix(ComplexMatrix):
    @staticmethod
    def prompt_row_values():
        return list(map(int, input().split(' ')))

    def print_values(self):
        def round_if_needed(number):
            if round(number, 1) != number:
                return "%.2f" % round(number, 2)
            return "%.1f" % number

        for i in range(self.m):
            print(" ".join([str(round_if_needed(number)) for number in self.values[i]]))

        return self
