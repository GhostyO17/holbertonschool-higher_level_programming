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
        """
        Rectangle args
        """
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
        """
        Validates if input is correct
        """
        if type(value) != (int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and name in ("width", "height"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and name in ("x", "y"):
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """
        Width property of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter for the propperty
        """
        self.integer_validator(value, "width")
        self.width = value

    @property
    def heigth(self):
        """
        Height property of the rectangle
        """
        return self.__height

    @heigth.setter
    def height(self, value):
        """
        height setter for the propperty
        """
        self.integer_validator(value, "height")
        self.heigth = value

    @property
    def x(self):
        """
        X property of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter for the propperty
        """
        self.integer_validator(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        Y property of the rectangle
        """
        return self.__x

    @y.setter
    def y(self, value):
        """
        y setter for the propperty
        """
        self.integer_validator(value, "y")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        displays in the stdout the rectangle
        """
        if self.__y > 0:
            for h in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Creates custom __str__ method
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )
