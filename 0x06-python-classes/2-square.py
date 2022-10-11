#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new quare

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__name = size
