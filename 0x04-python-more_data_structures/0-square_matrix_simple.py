#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    """ Compute the squre value of all integers of matrix """

    squre_value = [[v ** 2 for v in row] for row in matrix]

    return squre_value
