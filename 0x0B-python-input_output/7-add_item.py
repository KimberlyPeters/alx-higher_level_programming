#!/usr/bin/python3
"""
Add all arguments to a Python list and save them to a file.
"""

import sys

if __name__ == "__main__":
    # Import the necessary functions from the respective modules
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Try to load the existing list from the file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list
        items = []

    # Add all command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")
