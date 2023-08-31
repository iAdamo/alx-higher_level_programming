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

    @property
    def size(self):
        """size - (getter property) attribute data size

        Args:
            self: reference to the object instance

        Return:
            __size to an object instance
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """size - (setter property) set value to attribute self.__size

        Args:
            self: reference to object isinstaance
            value: data value to set to attributr __size
        Return:
            Nothing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area - calculate the current square area

        Args:
            self: reference to the instance of the class

        Return:
            the current square area
        """
        return ((self.__size) ** 2)

    def my_print(self):
        """my_print - prints in stdout the square with the character #

        Args:
            self - reference to th instance of the class

        Return:
            Nothing
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
        if self.__size == 0:
            print()
