#!/usr/bin/python3
"""module to define a rectangle"""


class Rectangle:
    """defined an empty Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints string when Instance deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter forprivate instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle defined"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of defined rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns a printable string rep of the rectangle defined"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns string rep of the rectngle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
