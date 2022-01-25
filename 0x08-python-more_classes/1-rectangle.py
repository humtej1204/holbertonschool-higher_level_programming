#!/usr/bin/python3

'''Here we learn more about Classes and Objects'''


class Rectangle:
    '''Class Rectangle'''
    def __init__(self, width=0, height=0):
        '''Initializing atributes'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Getting the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setting the value of width'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getting the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setting the value of height'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
