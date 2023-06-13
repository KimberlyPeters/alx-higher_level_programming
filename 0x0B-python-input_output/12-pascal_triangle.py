#!/usr/bin/python3
"""A module containing a pascal triangle function"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): The size of Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
