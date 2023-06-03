#!/usr/bin/python3
"""
This module is composed by a function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square of a given size using the character '#'.
    Args:
        size: An integer representing the size length of the square.
    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print('#' * size)
