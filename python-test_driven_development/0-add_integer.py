#!/usr/bin/python3
""" A function that adds two integers """


def add_integer(a, b=98):
    """      
    takes two numbers as input
    returns the sum or raises a TypeError if given the wrong parameter
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if type(b) == str:
        raise TypeError("b must be an integer")
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int):
            return a + b
