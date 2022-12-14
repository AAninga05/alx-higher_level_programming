#!/usr/bin/python3
"""Defines a square model Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update the class Square"""
        if args and len(args) != 0:
            arg_count = 0
            for arg in args:
                if arg_count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y,)
                    else:
                        self.id = arg
                elif arg_count == 1:
                    self.size = arg
                elif arg_count == 2:
                    self.x = arg
                elif arg_count == 3:
                    self.y = arg
            arg_count += 1
        elif kwargs and len(kwargs):
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

        def to_dictionary(self):
            """Return the dictionary representation of the Square."""
            return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
