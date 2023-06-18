#!/usr/bin/python3

"""
Module: models.base
Defines the Base class, which serves as the base
class for all other classes in this project.
"""

import json


class Base:
    """
    Base class for all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID of the instance. If provided, assigns
                      it to the id attribute.
                      If not provided, increments the __nb_objects counter
                      and assigns the new value to the id attribute.
                      Defaults to None.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): The list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
