#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
     A function that returns the list
     of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
