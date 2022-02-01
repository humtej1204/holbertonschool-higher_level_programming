#!/usr/bin/python3

'''Task 10 - 10. Square #1'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''Initializing atributes'''
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)
