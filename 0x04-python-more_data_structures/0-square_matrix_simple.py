#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return (matrix_square)
