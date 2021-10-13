#!/usr/bin/python3


"""
Scripts that save,add and load  to a file

"""


import json
import os.path


args = sys.argv[1:]

sv = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

item = []
if os.path.exists("./add_item.json"):
    item = load_json("add_item.json")

sv(item + args, "add_item.json")
