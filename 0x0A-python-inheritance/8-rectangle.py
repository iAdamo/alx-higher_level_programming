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
        super().integer_validator("width",self.__width)
