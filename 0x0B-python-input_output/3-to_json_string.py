#!/usr/bin/python3
"""
Module witch contain function that returns
the Json representation of an object
"""
import json


def to_json_string(my_obj):
    """ returns the object by converting it into a JSON string """
    return (json.dumps(my_obj))
