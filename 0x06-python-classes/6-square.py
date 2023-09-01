#!/usr/bin/python3
"""Square - class Square that defines a square"""


class Square:
    """Square - class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ - defines the attribute of an instance"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """size - (getter property) attribute data size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size - (setter property) set value to attribute self.__size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position - (getter property) attribute data size"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position - (setter property) set value to attribute self.__size"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area - calculate the current square area"""
        return ((self.__size) ** 2)

    def my_print(self):
        """my_print - prints in stdout the square with the character #"""
        a = self.__position[0]
        b = self.__position[1]
        for _ in range(b):
            print()
        for _ in range(self.__size):
            print(" " * a + '#' * self.__size)

        if self.__size == 0:
            print()
