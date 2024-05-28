#!/usr/bin/python3
""" 
Square class
"""

class Square:
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Calculate the area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Calculate the perimeter of the square """
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())

