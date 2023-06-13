#!/usr/bin/python3
"""
This module contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file to load the object from.

    Returns:
        The object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
