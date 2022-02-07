#!/usr/bin/python3
'''Rectangle Class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Inicilizating ATRIBUTES
        Inheriting attribute ID'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.check_wh("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.check_wh("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.check_xy("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.check_xy("y", y)
        self.__y = y

    def check_wh(self, n, a):
        '''Method that check the values of width and height'''
        if type(a) is not int:
            raise TypeError("{} must be an integer".format(n))
        if a <= 0:
            raise ValueError("{} must be > 0".format(n))
        return

    def check_xy(self, n, a):
        '''Method that check the values of x and y'''
        if type(a) is not int:
            raise TypeError("{} must be an integer".format(n))
        if a < 0:
            raise ValueError("{} must be >= 0".format(n))
        return

    def area(self):
        '''Method that returns the area value of the Rectangle instance'''
        return (self.width * self.height)

    def display(self):
        '''Method that print in stdout the Rectangle instance with the
        character # by taking care of x and y'''
        print("\n" * self.y, end="")
        tx = " " * self.x
        pnt = (("#" * self.width) + "\n")
        print((tx + pnt) * self.height, end="")

    def __str__(self):
        '''Method that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        t1 = "[Rectangle]"
        t2 = " ({}) {}/{}".format(self.id, self.x, self.y)
        t3 = " - {}/{}".format(self.width, self.height)
        return (t1 + t2 + t3)

    def update(self, *args, **kwargs):
        '''Method that assigns a value to each attribute'''
        # Manera en la cual creas una lista con cada nombre de cada
        # atributo y busca su existencia en el objeto
        if len(args) > 0:
            key = ["id", "width", "height", "x", "y"]
            for x in range(len(args)):
                setattr(self, key[x], args[x])
        # Manera en la cual busca todos los attributos del objeto
        # y los convierte en una lista
        '''for i in range(len(args)):
                setattr(self, list(self.__dict__.keys())[i], args[i])'''

        if len(args) == 0:
            for x in kwargs:
                setattr(self, x, kwargs[x])
            '''for attr in kwargs:
                if hasattr(self, attr):
                    setattr(self, attr, kwargs[attr])'''

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Rectangle'''
        key = ["id", "width", "height", "x", "y"]
        value = list(self.__dict__.values())
        return dict(zip(key, value))
