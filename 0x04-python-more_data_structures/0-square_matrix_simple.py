#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup_matrix = matrix.copy()
    for line in range(len(matrix)):
        dup_matrix[line] = list(map((lambda x: x**2), matrix[line]))
    return(dup_matrix)
