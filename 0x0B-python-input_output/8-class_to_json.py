#!/usr/bin/python3
"""
a program that contain a function that returns
the dictionary description for JSON of an object
"""


def class_to_json(obj):
    """
    returns the dictionary descritpion of JSON object
    """
    return obj.__dict__
