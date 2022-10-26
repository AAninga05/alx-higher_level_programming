#!/usr/bin/python3
"""Defines a class Mylist"""

class MyList(list):
    """Defines a class my list"""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
