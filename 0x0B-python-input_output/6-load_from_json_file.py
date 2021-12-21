#!/usr/bin/python3
"""
a program Creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from JSON"""
    with open(filename, encoding='utf-8') as filestreamobject:
        return json.load(filestreamobject)
