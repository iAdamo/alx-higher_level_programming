#!/usr/bin/python3
"""
This is the 9-student module
It supplies Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize instances to class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """
        return vars(self)
