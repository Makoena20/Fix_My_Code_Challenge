#!/usr/bin/python3
""" Module for Square class """

 class Square:
    """Class Square defines a square"""

    def __init__(self, width):
        """Instantiation with width"""
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a non-negative number")
        self.__width = width

    def area(self):
        """Returns the area of the square"""
        return self.__width * self.__width

