#!/usr/bin/python3
"""a module that contains a function"""


def add_attribute(object, attribute, attvalue):
    """A function that adds a new attribute to
    an object if it’s possible
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, attvalue)
