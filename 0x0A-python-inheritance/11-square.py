#!/usr/bin/python3

'''Task 11 - 11. Square #2'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''

    def __init__(self, size):
        '''Initializing atributes'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''Defining __str__ Method'''
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
