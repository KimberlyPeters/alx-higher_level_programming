#!/usr/bin/python3
"""
This module contains a function is_same_class that checks if an object is
exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        False otherwise.

    Raises:
        None
    """
    return type(obj) is a_class
