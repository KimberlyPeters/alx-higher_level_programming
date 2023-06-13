#!/usr/bin/python3
"""
This module contains a function that writes a string to a
text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and
    returns the number of characters written.

    Args:
        filename (str): The name of the text file to write to (optional).
        text (str): The string to write to the file (optional).

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written
