#!/usr/bin/python3
"""
Module with a script that adds arguments
to a Python list saved in a file
"""

import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if os.path.exists(filename):
    list = load_from_json_file(filename)
    list.extend(sys.argv[1:])
    save_to_json_file(list, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
