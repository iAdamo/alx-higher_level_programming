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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        new_dict = {}
        my_dict = vars(self)
        if not isinstance(attrs, list):
            return vars(self)
        for each_attr in attrs:
            if isinstance(each_attr, str):
                for key, value in my_dict.items():
                    if key is each_attr:
                        new_dict[key] = value
            else:
                return vars(self)
        return new_dict
