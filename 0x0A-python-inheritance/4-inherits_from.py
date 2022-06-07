#!/usr/bin/python3
"""returns True if an object is an instance of class inherited from a class"""


def inherits_from(obj, a_class):
    """"""
    if isinstance(obj, a_class) and\
            issubclass(a_class, obj.__class__) is False:
        return True
    return False
