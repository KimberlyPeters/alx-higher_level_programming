#!/usr/bin/python3

"""
Module: models.square
Defines the Square class, which inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    Represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position. Defaults to 0.
            y (int): The y-coordinate of the square's position. Defaults to 0.
            id (int): The ID of the square. Defaults to None.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the square in the format:
                "[Square] (<id>) <x>/<y> - <size>"
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
