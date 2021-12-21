#!/usr/bin/python3
"""
Module that contains a function that returns an
object represented by Json string
"""
import json


def from_json_string(my_str):
    """parses JSON string, convert in to python dictionary
    and returns dictionary object
    """
    return json.loads(my_str)
