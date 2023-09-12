#!/usr/bin/python3
"""The 8-rectangle: python inheritance

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/7-base_geometry.txt | tail -2) to test
Remove the pipeline to see full details
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class Rectangle to parent class BaseGeometry"""
    def __init__(self, width, height):
        """initialize an object instance"""
        self.__width = width
        self.__height = height
        super().integer_validator("height", self.__height)
        super().integer_validator("width", self.__width)

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns an informal string representation of an instance"""
        return f"[Rectangle] {self.__width}/{self.__height}"
