#!/usr/bin/python3

'''Task 10 - 10. Student to JSON with filter'''


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        '''Inicilizating ATRIBUTES'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary of Student"""

        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            tmp = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    tmp[i] = self.__dict__[i]
            return tmp
