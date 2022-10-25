#!/usr/bin/python3
"""Defines a class Mylist"""

class MyList(list):

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
