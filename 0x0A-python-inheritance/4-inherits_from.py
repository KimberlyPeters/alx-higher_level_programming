#!/usr/bin/python3
"""
This module contains a function inherits_from that checks if an object is
an instance of a class that inherited (directly or indirectly) from the
specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class;
        False otherwise.

    Raises:
        None
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
