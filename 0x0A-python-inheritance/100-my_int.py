#!/usr/bin/python3
"""100-my_int - python inheritance"""


class MyInt(int):
    """class MyInt that inherits from `int`"""
    def __eq__(self, num):
        """__eq__: computes equality
        Return: not equally bool"""
        return not super().__eq__(num)

    def __ne__(self, num):
        """__ne__: computes inequality
        Return: not inquality bool"""
        return not super().__ne__(num)
