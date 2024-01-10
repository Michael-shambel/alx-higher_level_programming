#!/usr/bin/python3
"""Define that this function divide all elements in the matrix"""


def matrix_divided(matrix, div):
    """ divide every element of the matrix
    raise :
    TypeError: if it is not list of intiger or float
    TypeError: if the matrix is not ame size
    TypeError: div must be number
    ZeroDivisionError: div must be different from 0
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                    )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        n_matrix = [round(num / div, 2) for num in row]
        new_matrix.append(n_matrix)

    return new_matrix
