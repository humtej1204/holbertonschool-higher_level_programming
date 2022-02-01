#!/usr/bin/python3

'''Task 09 - 9. Student to JSON'''


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        '''Inicilizating ATRIBUTES'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary of Student"""
        return self.__dict__
