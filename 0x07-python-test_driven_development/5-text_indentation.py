#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each
    occurrence of '.', '?', and ':' characters.

    Args:
        text (str): Input string.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.
    """

    # Check if text is a string
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]  # Create a copy of the input text

    # Split the text by '.', '?', and ':' characters
    # and insert 2 new lines after each occurrence
    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            # Remove leading and trailing spaces from each sentence
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
