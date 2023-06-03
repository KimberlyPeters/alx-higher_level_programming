#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':' characters.
    Args:
        text: A string representing the input text.
    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences using '.', '?', and ':' as delimiters
    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence += char
        if char in ['.', '?', ':']:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    # Print the sentences with 2 new lines after each
    for sentence in sentences:
        print(sentence)
        print()
