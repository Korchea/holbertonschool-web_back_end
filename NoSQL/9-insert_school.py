#!/usr/bin/env python3
""" Python function that inserts a new document in a
collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ Python function that inserts a new document in a
    collection based on kwargs"""
    in_dict = {}
    for arg in kwargs:
        arg.replace('=', ": ")
        arg = '{' + arg + '}'
        in_dict.update(arg)
    return mongo_collection.insert_one(in_dict)
