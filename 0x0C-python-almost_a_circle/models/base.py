#!/usr/bin/python3
"""
base module
Supplies the Base class.

Run "python3 -m unittest tests/test_models/test_base.py" for unittest
"""

import json
from os.path import exists


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The unique identifier for the
            instance (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be
            converted to JSON.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file.

        Args:
            cls: The class (automatically provided by Python).
            list_objs (list): A list of objects to be saved to a file.
        """
        
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as out:
            if list_objs is None:
                out.write([])
            else:
                outlist = []
                for each_instance in list_objs:
                    outlist.append(each_instance.to_dictionary())
                out.write(cls.to_json_string(outlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of dictionaries from a JSON string representation.

        Args:
            json_string (str): A JSON string representing a
            list of dictionaries.

        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes set using a dictionary.

        Args:
            dictionary (dict): A dictionary containing attribute-value pairs.

        Returns:
            cls: An instance of the class with attributes
            set from the dictionary.
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns a list of instances.

        Returns:
            list: A list of instances created from the data in the JSON file.
        """
        filename = cls.__name__ + ".json"
        if not exists(filename):
            return []
        else:
            new_id = []
            with open(filename, 'r', encoding='utf-8') as out:
                json_string = out.readline()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**each_dict) for each_dict in dict_list]
