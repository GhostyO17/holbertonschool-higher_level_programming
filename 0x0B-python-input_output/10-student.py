#!/usr/bin/python3
"""
Define class method
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name='', last_name='', age=0):
        """
        Method that assigns public attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns:
            Dictionary representation of a Student instance
        """
        obj_d = dict()
        if type(attrs) is list:
            for obj in attrs:
                if type(obj) is not str:
                    return self.__dict__

                if obj in self.__dict__:
                    obj_d[obj] = self.__dict__[obj]

            return obj_d

        return self.__dict__
