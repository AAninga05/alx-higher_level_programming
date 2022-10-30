#!/usr/bin/python3
"""Describes a base model Class"""


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
