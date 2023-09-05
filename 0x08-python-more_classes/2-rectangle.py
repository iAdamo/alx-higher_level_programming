#!/usr/bin/python3

"""
0-rectangle.py module - contains Rectangle() class
"""


class Rectangle():
    """Rectangle - mpty class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter peoperty width - returns private instance __width"""
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
        """getter peoperty height - returns private instance __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property width - sets value to
        private instance attribute __height"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        """area: public instance method that returns the rectangle area"""
        return ((self.__width) * (self.__height))

    def perimeter(self):
        """perimeter: public instance method that
        returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))