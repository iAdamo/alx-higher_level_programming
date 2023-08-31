#!/usr/bin/python3
"""Square - class Square that defines a square"""


class Square:
    """Square - class Square that defines a square"""
    def __init__(self, size=0):
        """__init__ - defines the attribute of an instance

        Args:
            self: A reference to the object instance
            size: size of the square

        Return:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area - calculate the current square area

        Args:
            self: reference to the object instance

        Return:
            the current square area
        """
        return ((self.__size) ** 2)
