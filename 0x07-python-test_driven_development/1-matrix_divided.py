#!/usr/bin/python3
""" defining matrix devider
"""


def matrix_divided(matrix, div):
    """
    Divide all elements in the matrix.

    Matrix must be a list of lists of integers or floats.

    Otherwise:
    raise TypeError with a given exception message.

    Each row of the matrix must be the same size, else...
    raise TypeError with given message.

    div must be a number (integer or float).

    Otherwise:
    raise TypeError with a given exception message.

    div must not be == 0, if so raise ZeroDivisionError
    with a given exception message.

    All elements of the matrix should be divided by div
    rounded to 2 decimal places.

    Then return the new matrix.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("each row of matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
