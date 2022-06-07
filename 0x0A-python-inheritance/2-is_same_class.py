#!/usr/bin/python3
"""Test if and object is of a given class"""


def is_same_class(obj, a_class):
    """ is_same_class Returns true if object is of a given class """
    if type(obj) is a_class:
        return True
    else:
        return False
