#!/usr/bin/python3
"""Describes a base model Class"""
import json

class Base:
    """Represents base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    def save_to_file(cls, list_objs):

