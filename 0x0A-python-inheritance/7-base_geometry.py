#!/usr/bin/python3
"""The 5-base_geometry: python inheritance

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/7-base_geometry.txt | tail -2) to test
Remove the pipeline to see full details
"""


class BaseGeometry():
    """class BaseGeometry"""
    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value input"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
