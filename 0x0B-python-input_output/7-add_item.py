#!/usr/bin/python3
"""
A module of function that adds all arguments to a Python list then save it
"""

import json
import sys
import os.path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_filea = "add_item.json"

my_ites = []

if os.path.exists(my_filea) and os.path.getsize(my_filea) > 0:
    my_ites = load_from_json_file(my_filea)

if len(sys.argv) > 1:
    for lis in sys.argv[1:]:
        my_ites.append(lis)

save_to_json_file(my_ites, my_filea)
