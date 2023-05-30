#!/usr/bin/python3
"""Validates the size of a square and computes its area"""


class Square():
    """Defines a square and validates its size"""

    def __init__(self, size=0):
        """
        Initializes the square

        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)
