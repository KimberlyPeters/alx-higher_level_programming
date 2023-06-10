#!/usr/bin/python3
"""
This module contains a function that adds a new
attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add the attribute to.
        attr (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.

    Returns:
        None
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
