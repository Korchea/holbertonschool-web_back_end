#!/usr/bin/env python3
""" Python function that changes all topics of a school
document based on the name"""


def update_topics(mongo_collection, name, topics):
    """ Python function that changes all topics of a school
    document based on the name"""
    newValues = {}
    for topic in topics:
        newValues.update({"topics": topic})
    mongo_collection.update_many({"name": name}, {"$set": newValues})
