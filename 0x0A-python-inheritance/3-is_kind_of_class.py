#!/usr/bin/python3
"""
Module that contains a function that check if an object
is an instance of or object is an instance of a class
that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns true of an object is an instance of
    a class or of its super class otherwise false
    """
    return (isinstance(obj, a_class))
