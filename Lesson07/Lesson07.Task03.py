class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        new_count = self.count + other.count
        return Cell(new_count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            new_count = self.count - other.count
            return Cell(new_count)
        else:
            raise ValueError('Невозможно вычесть!')

    def __mul__(self, other):
        new_count = self.count * other.count
        return Cell(new_count)

    def __truediv__(self, other):
        new_count = self.count // other.count
        return Cell(new_count)

    def make_order(self, number):
        l = ''
        c = 0
        for i in range(self.count):
            l += '*'
            c += 1
            if c == number:
                l += '\n'
                c = 0
        return (l)


cell_1 = Cell(5)
cell_2 = Cell(24)

cell_3 = cell_2 + cell_1

print(cell_2.make_order(5))
