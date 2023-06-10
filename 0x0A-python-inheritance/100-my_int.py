#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class representing a rebel integer.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==) to be inverted.

        Args:
            other (int): The value to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to be inverted.

        Args:
            other (int): The value to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
