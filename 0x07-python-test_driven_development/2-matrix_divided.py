#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.
    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (integer or float) to divide the elements by.
    Returns:
        A new matrix with elements divided by div, rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division of matrix elements by div, rounded to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return (new_matrix)
