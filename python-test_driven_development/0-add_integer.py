#!/usr/bin/python3
""" A function that adds two integers """


def add_integer(a, b=98):
    """
    takes two numbers as input
    returns the sum or raises a TypeError if given the wrong parameter
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not type(a) in (int, float):
        raise TypeError('a must be an integer')

    if not type(b) in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
