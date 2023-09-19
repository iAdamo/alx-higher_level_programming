#!/usr/bin/python3
"""
base module
Supplies the Base class.

Run "python3 -m unittest tests/test_models/test_base.py" for unittest
"""

import json
import csv
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
                out.write('[]')
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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be serialized.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as outcsv:
            dict_obj = [each_obj.to_dictionary() for each_obj in list_objs]
            for each_dict in dict_obj:
                fieldnames = [key for key in each_dict]
            file_csv = csv.DictWriter(outcsv, fieldnames=fieldnames)
            file_csv.writeheader()
            for each_dict in dict_obj:
                file_csv.writerow(each_dict)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file.

        Returns:
            list: A list of object instances created from the CSV data.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            instance_list = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                    instance = {field: int(row[field]) for field in fields}
                if cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                    instance = {field: int(row[field]) for field in fields}
                instance_list.append(instance)

        return [cls.create(**each_dict) for each_dict in instance_list]
