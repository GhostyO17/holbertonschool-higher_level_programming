#!/usr/bin/python3
"""Creates an empty class"""


class BaseGeometry:
    """ area - create empty area """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(str(name)))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(str(name)))


class Rectangle(BaseGeometry):
    """Creates a Rectangle subclass of BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
