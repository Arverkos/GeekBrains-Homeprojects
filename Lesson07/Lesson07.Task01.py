class Matrix:
    def __init__(self, list):
        self.matrix = list

    def __str__(self):
        print_matrix = ''
        for line in self.matrix:
            l = ' '.join([str(el) for el in line])
            print_matrix += l + '\n'
        return print_matrix

    def __add__(self, other):
        new_line = []
        new_mat = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_el = self.matrix[i][j] + other.matrix[i][j]
                new_line.append(new_el)
            new_mat.append(new_line)
            new_line = []

        return Matrix(new_mat)


a = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

b = [[2, 5, 2],
     [2, 2, 2],
     [2, 8, 2]]

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(matrix_1)
print(matrix_2)

matrix_3 = matrix_1 + matrix_2

print(matrix_3)
