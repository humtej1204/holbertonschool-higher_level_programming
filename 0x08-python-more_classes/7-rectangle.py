#!/usr/bin/python3
"""Change representation"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the data"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the position"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Return a string with rectangle to stdout"""
        _str = ""
        if self.height == 0 or self.width == 0:
            return ''
        for i in range(self.height):
            _str += str(self.print_symbol) * self.width
            if self.height != i + 1:
                _str += '\n'
        return _str

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints the message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
