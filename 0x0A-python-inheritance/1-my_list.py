#!/usr/bin/python3

"""A module that shows how to inherit in  python"""


class MyList(list):
    """Mylist - class that inherit the class of 'list'"""
    def print_sorted(self):
        """ method to sort a list"""
        print(sorted(self))
