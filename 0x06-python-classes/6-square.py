#!/usr/bin/python3
""" Define an object name Square.
"""


class Square:
    """ Object Square [class]
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method - Initialize.
        Args:
            self (class): This class
            size (int): Size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """ Method - Returns the current square area.
        Args:
            self (class): This class
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method - prints in stdout the square with the character #.
        Args:
            self (class): This class
        """
        if self.__size:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()

    @property
    def size(self):
        """ Get - instance attribute size
        """
        return (self.__size)

    @property
    def position(self):
        """ Get - instance attribute position
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """ Set - instance attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Set - instance attribute position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
