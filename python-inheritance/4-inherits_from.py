#!/usr/bin/python3
"""
returns True if an object is an instance of class inherited from a class
"""


def inherits_from(oj, a_class):
    """
    Returns: True if the object is an instance of class inherited from a class
    """
    if isinstance(oj, a_class) and issubclass(a_class, oj.__class__) is False:
        return True
    return False
