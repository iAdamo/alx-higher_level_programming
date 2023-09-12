#!/usr/bin/python3
"""10-square module
Author: Adam Sanusi Babatunde
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square of subclass Rectangle"""
    def __init__(self, size):
        """ initialize an instance"""
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """returns an informal represantation of an instance"""
        return f"[Rectangle] {self.__size}/{self.__size}"
