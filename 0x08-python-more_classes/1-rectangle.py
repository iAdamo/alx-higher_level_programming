#!/usr/bin/python3

"""
0-rectangle module - contains Rectangle() class
"""


class Rectangle():
    """Rectangle - empty class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = 0  # private instance attribute
        self.__height = 0  # private instance attribute
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter property width - returns private instance __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property width - sets value to
        private instance attribute __height"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter property height - returns private instance __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property height - sets value to
        private instance attribute __height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
