#!/usr/bin/python3

'''Task 11 - 11. Square #2'''


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


class Rectangle(BaseGeometry):
    '''class Rectangle'''

    def __init__(self, width, height):
        '''Initializing atributes'''
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        '''Function that return the rectangle area'''
        return self.__width * self.__height

    def __str__(self):
        '''Defining __str__ Method'''
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string


class Square(Rectangle):
    '''class Square'''

    def __init__(self, size):
        '''Initializing atributes'''
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)

    def __str__(self):
        '''Defining __str__ Method'''
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
