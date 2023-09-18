#!/usr/bin/python3
"""
base.py module
supplies base class
"""
import json
from os.path import exists


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor: initialize the class instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        for class_name in list_objs:
            filename = class_name.__class__.__name__ + ".json"
            with open(filename, 'w', encoding='utf-8') as out:   
                if list_objs is None:
                    out.write('[]')
                else:
                    outlist = []
                    for each_instance in list_objs:
                        outlist.append(each_instance.to_dictionary())
                    out.write(cls.to_json_string(outlist))
                
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        
        Args:
            json_string: is a string representing a list of dictionaries

        Return:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string == None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        
        Args:
            dictionary: can be thought of as a double pointer to a dictionary
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not exists(filename):
            return []
        else:
            with open(filename, 'r')
