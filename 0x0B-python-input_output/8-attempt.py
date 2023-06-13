#!/usr/bin/python3
"""
Returns the dictionary description with simple
data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """Converts an object to a dictionary with a
    simple data structure for JSON serialization."""
    # Check if the object has a __dict__ attribute
    if hasattr(obj, "__dict__"):
        # Get the object's dictionary representation
        obj_dict = obj.__dict__.copy()
        # Convert each attribute value to a JSON-serializable format
        for key, value in obj_dict.items():
            # Convert lists and dictionaries recursively
            if isinstance(value, (list, dict)):
                obj_dict[key] = class_to_json(value)
            # Convert boolean values to lowercase strings
            elif isinstance(value, bool):
                obj_dict[key] = str(value).lower()
            # Convert all other values to their string representation
            else:
                obj_dict[key] = str(value)
        return obj_dict
    else:
        # If the object doesn't have a __dict__ attribute, return None
        return None
