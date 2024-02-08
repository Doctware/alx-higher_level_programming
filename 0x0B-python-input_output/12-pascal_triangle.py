#!/usr/bin/python3
""" this function return list og integers reprecentig
    the pascal's triangle """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list of lists of int: A list of lists representing Pascal's triangle.
                              Each inner list represents a row of the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            # Generate other elements of the row based on the previous row
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
