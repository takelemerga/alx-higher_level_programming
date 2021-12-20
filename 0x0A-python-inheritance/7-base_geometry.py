#!/usr/bin/python3
"""
Module for a BaseGeometry class
"""


class BaseGeometry:
    """
    defines class BaseGeometry with unimplemented method area()
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
