#!/usr/bin/python3
"""
    define width and height properties for Rectangle class.
"""


class Rectangle:
    """
    Rectangle with height and width properties.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ Defines property width. """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ Defines property height. """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
