#!/usr/bin/python3
"""
Creates rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    Creates rectangle class with several attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.integer_validator(width, "width")
        self.integer_validator(height, "height")
        self.integer_validator(x, "x")
        self.integer_validator(y, "y")
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def integer_validator(self, value, name):
        if type(value) != (int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and name in ("width", "height"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and name in ("x", "y"):
            raise ValueError(f"{name} must be >= 0")
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator(value, "width")
        self.width = value

    @property
    def heigth(self):
        return self.__height

    @heigth.setter
    def height(self, value):
        self.integer_validator(value, "height")
        self.heigth = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__x

    @y.setter
    def y(self, value):
        self.integer_validator(value, "y")
        self.__y = value
    
    def area(self):
        return (self.__width * self.__height)

    def display(self):
        if self.__height > 0:
            for i in range(self.__height):
                print(end='')

        for i in range(self.__height):
            if self.__width > 0:
                print(end='')

            for j in range(self.__width):
                print('#', end='')

            print()