#!/usr/bin/python3

"""
0-rectangle module - contains Rectangle() class
"""


class Rectangle():
    """Rectangle - empty class Rectangle that defines a rectangle"""

    number_of_instances = 0  # public class attribute
    print_symbol = '#'  # public class attribute

    def __init__(self, width=0, height=0):
        """__init__: a setup or initialization method for objects"""
        self.__width = 0  # private instance attribute
        self.__height = 0  # private instance attribute
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """__str__: instance method that return an informal string
        representation of an instance"""
        rect = str()
        for _ in range(self.__height):
            rect += str(self.print_symbol) * self.__width + '\n'
        return rect[:-1]

    def __repr__(self):
        """__repr__: instance method that returns a formal string
        representation of an instance"""
        return f"Rectangle{(self.__width, self.__height)}"

    def __del__(self):
        """__del__: instance method that does a custom clean up"""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
