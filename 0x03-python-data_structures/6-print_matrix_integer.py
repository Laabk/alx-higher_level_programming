#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for d in range(len(matrix)):
        for a in range(len(matrix[d])):
            if a != 0:
                print(" ", end='')
            print("{:d}".format(matrix[d][a]), end='')
        print()
