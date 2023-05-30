#!/usr/bin/python3
"""Represents a square with a private size attribute"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size):
        """initialize square
        Args:
            size (int): size of the square
        """
        self.__size = size  #: size of the square
