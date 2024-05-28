#!/usr/bin/python3

class Square:
    
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Size must be a non-negative value")
        self._size = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def perimeter_of_my_square(self):
        return self.size * 4

    def __str__(self):
        return "{}/{}".format(self.size, self.size)

if __name__ == "__main__":

    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

