#!/usr/bin/python3

'''Task 10 - 10. Square #1'''


class BaseGeometry():
    '''class BaseGeometry'''

    def area(self):
        '''Function that raises an Exception with the message area()
        is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''that validates value:
        if value is not an integer: raise a TypeError exception
        if value is less or equal to 0:
        raise a ValueError exception with the message'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Square(Rectangle):
    """Class Square that inherits from Rectangle (9-rectangle.py):"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
