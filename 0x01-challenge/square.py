#!/usr/bin/python3

class Square:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PerimeterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return f"Square: {self.width}/{self.height}"

if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())

