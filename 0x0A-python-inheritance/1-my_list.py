#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
