#!/usr/bin/python3

'''Task 07 - 7. Integer validator'''


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
