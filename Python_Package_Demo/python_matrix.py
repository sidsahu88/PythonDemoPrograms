matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix(matrix):
    for row in matrix:
        matrix_row = ''
        for i in row:
            matrix_row += str(i) + ' '
        print(matrix_row)


print("Matrix: ")
print_matrix(matrix)

print(f'Matrix[1][0]: {matrix[1][0]}')

matrix[1][0] = 40

print(f'Matrix[1][0]: {matrix[1][0]}')

print("New Matrix: ")
print_matrix(matrix)
