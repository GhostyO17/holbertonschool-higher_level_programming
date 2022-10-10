#!/usr/bin/python3
"""
    define width and height properties for Rectangle class.
"""


class Rectangle:
    """
    Rectangle with height and width properties.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    """ __str__ & __repr__ Method """
    def __str__(self):
        str_n = ""
        if self.height == 0 or self.width == 0:
            return str_n
        for i in range(self.height):
            for j in range(self.width):
                str_n += "#"
            if i == self.height - 1:
                break
            str_n += "\n"
        return str_n

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    """ Delete method """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ Area and perimeter method. """
    def area(self):
        a = int(self.height * self.width)
        return (a)

    def perimeter(self):
        if int(self.height) == 0 or int(self.width) == 0:
            p = 0
        else:
            p = int(2 * (self.height + self.width))
        return (p)

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
