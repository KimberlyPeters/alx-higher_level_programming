#!/usr/bin/python3

"""
Module: models.base
Defines the Base class, which serves as the base
class for all other classes in this project.
"""


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
