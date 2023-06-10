#!/usr/bin/python3
"""
This module contains a function is_kind_of_class that checks if an object is
an instance of, or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class;
        False otherwise.

    Raises:
        None
    """
    return isinstance(obj, a_class)
