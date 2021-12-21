#!/usr/bin/python3
"""
Module that contains a class Student
"""


class Student:
    """ defines Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns student dictionary data struct """
        dic = {}
        if attrs is None:
            return self.__dict__
        dic = dict()
        for key in attrs:
            if key in self.__dict__.keys():
                dic[key] = self.__dict__[key]
        return dic

    def reload_from_json(self, json):
        """
        public method that replaces all
        attributes of the Student instance
        """
        return self.__dict__.update(json)
