#!/usr/bin/python3
"""
A function that prints a square made of '#'
"""



def print_square(size):
    """A function that prints a square made of '#'
    """
    errt1 = "size must be an integer"
    errv = "size must be >= 0"

    if not type(size) is (int):
        raise TypeError(errt1)
    if size < 0:
        raise ValueError(errv)
    if type(size) is (float) and size < 0:
        raise TypeError(errt1)

    for i in range(0, size):
        for z in range(0, size):
            print('#', end='')
        print()
