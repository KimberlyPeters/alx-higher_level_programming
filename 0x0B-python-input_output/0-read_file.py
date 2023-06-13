#!/usr/bin/python3
"""
This module contains a function that reads a
text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to read (optional).

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents, end='')
