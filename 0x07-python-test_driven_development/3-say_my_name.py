#!/usr/bin/python3
"""
This module is composed by a function prints a message
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".
    Args:
        first_name: A string representing the first name.
        last_name: (Optional) A string representing the last name.
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print(f"My name is {first_name} {last_name}")
