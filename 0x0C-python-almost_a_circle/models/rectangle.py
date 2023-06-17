#!/usr/bin/python3

"""
Module: models.rectangle
Defines the Rectangle class, which inherits from Base.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int): The ID of the rectangle. Defaults to None.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width of the rectangle.

        Returns:
            None
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height of the rectangle.

        Returns:
            None
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute.

        Args:
            value (int): The x-coordinate of the rectangle's position.

        Returns:
            None
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute.

        Args:
            value (int): The y-coordinate of the rectangle's position.

        Returns:
            None
        """
        self.__y = value
