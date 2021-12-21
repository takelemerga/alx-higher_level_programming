#!/usr/bin/python3
"""
a program that contains a class Student
"""


class Student:
    """ defines Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns student dictionary data struct """
        return self.__dict__
