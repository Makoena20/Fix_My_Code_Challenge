#!/usr/bin/python3
""" Module for Square class """

class Square():
    """ Square class """
    def __init__(self, *args, **kwargs):
        """ Instantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perimeter of the square """
        return self.width * 4

    def __str__(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12)
    print(s)
    print(s.area())
    print(s.perimeter())

