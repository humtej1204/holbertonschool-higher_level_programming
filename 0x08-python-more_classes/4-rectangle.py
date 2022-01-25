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

    def area(self):
        '''Defining a method to get the area of the Rectangle'''
        return (self.height * self.width)

    def perimeter(self):
        '''Defining a method to get the perimeter of the Rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.height + self.width) * 2)

    def __str__(self):
        '''Defining __str__ Method'''
        if self.height == 0 or self.width == 0:
            return ""
        else:
            printable = ((("#" * self.width) + "\n") * self.height)
            return (printable[:-1])
            # return(((("#" * self.width) + "\n") * self.height)[:-1])

    def __repr__(self):
        '''Defining __repr__ Method'''
        return "Rectangle({}, {})".format(self.width, self.height)
        # return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
