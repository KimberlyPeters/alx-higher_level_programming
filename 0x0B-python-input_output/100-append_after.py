#!/usr/bin/python3
""" Module that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file
    after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert.

    Returns:
        None
    """
    new_file = ""

    with open(filename) as file:
        for line in file:
            new_file += line
            if search_string in line:
                new_file += new_string

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(new_file)
