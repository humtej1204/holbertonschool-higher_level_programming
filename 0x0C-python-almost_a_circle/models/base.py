#!/usr/bin/python3
'''Base Class'''
import json


class Base():
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Inicilizating ATRIBUTES'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        dc = []
        if list_objs:
            for x in list_objs:
                dictionary = x.to_dictionary()
                dc.append(dictionary)
        with open(filename, mode='w', encoding="utf-8") as f:
            s = cls.to_json_string(dc)
            f.write(s)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            ls = []
            return ls
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        f = cls.__name__ + ".json"
        ls = []
        try:
            with open(f, 'r') as file:
                x = file.read()
                y = cls.from_json_string(x)
                for a in range(len(y)):
                    z = cls.create(**y[a])
                    ls.append(z)
            return ls
        except Exception:
            return ls
