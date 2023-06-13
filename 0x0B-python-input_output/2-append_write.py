#!/usr/bin/python3
"""
This module contains a function that appends a string at the
end of a text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.

    Args:
        filename (str): The name of the text file to append to (optional).
        text (str): The string to append to the file (optional).

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
        return characters_added
