#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """ Print the matrix integer """

    for row in matrix:
        print(" ".join("{:d}".format(colum) for colum in row))
