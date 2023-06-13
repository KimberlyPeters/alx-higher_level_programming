#!/usr/bin/python3
"""
This module contains a function that writes an
object to a text file using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved.
        filename: The name of the file to save the JSON representation to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
