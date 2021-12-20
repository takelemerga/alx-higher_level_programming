#!/usr/bin/python3
"""
a module that contains a class Rectangle
that inherits from BaseGeometry class
"""


class BaseGeometry:
    """
    defines BaseGeomety class with unimplemented method area()
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
    rectangle class that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
