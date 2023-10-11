#!/usr/bin/python3
'2d simple square matrix'
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
