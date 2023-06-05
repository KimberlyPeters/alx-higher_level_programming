#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns their sum.
    Args:
        a: An integer or float to be added
        b: An integer or float to be added (default value is 98)
    Returns:
        An integer representing the sum of a and b
    Raises:
        TypeError: If a or b is not an integer and/or float
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Add the integers a and b
    result = a + b

    # Return the sum of a and b
    return result
