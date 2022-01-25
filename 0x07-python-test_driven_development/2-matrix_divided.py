#!/usr/bin/python3

"""Creting the Function matrix_divided"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    mtx = []
    c = 0

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(len(matrix)):
        mtx.append([])
        for k in matrix[i]:
            if type(k) not in [int, float]:
                t1 = 'matrix must be a matrix (list of lists)'
                t2 = ' of integers/floats'
                raise TypeError(t1 + t2)
            c = k / div
            c = round(c, 2)
            mtx[i].append(c)
    return mtx
