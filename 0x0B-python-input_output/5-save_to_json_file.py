#!/usr/bin/python3
"""
Module witch contain function that writes an
Object to a text file (with JSON)
"""
import json


def save_to_json_file(my_obj, filename):
    """ write object to text file using JSON"""
    with open(filename, mode='w') as filestreamobject:
        filestreamobject.write(json.dumps(my_obj))
