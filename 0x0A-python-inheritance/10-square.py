#!/usr/bin/python3

'''Task 10 - 10. Square #1'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        '''Initializing atributes'''
        super().__init__(size, size)
        super().integer_validator("size", size)
