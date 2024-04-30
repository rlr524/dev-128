"""In this assignment you will write two classes: A Point class and a Rectangle class
to represent a point and a rectangle in a 2-dimensional coordinate space. You will
write the definitions for these two classes so that the client code provided in
RectangleClient.py file works as expected. See Appendix for more information on the
coordinate system these points and rectangles are expected to be placed. Specifically,
1. Create a Point class with the following requirements:  Attributes: o __x:
x-coordinate of the point o __y: y-coordinate of the point  Two readonly Properties: o
x: x-coordinate of the point o y: y-coordinate of the point  A constructor: o This
takes two required arguments: x and y coordinates  One Method: o translate(dx,
dy): method moves the point by dx in x-direction and by dy in y direction (it updates
the __x and __y attributes by adding dx and dy to them respectively) 2. Create a
Rectangle class with the following requirements:  Three static attributes: o
DEFAULT_WIDTH (initialized to 1) o DEFAULT_HEIGHT (initialized to 1) o rectangleCount (
initialized to 0, represents the count of rectangles instantiated so far)  Attributes:
o __topLeft: an instance of Point class that denotes the top-left corner of the
rectangle. o __width: width of the rectangle (cannot be negative or 0) o __height:
height of the rectangle (cannot be negative or 0)  Three properties: o topLeft: Getter
should return the __topLeft attribute and the setter should update the __topLeft
attribute. o width: The getter method should return the __width attribute. Knowing that
__width cannot be negative or 0, the setter should check if client tries to set an
invalid value, if so, the setter should print a meaningful message, and not update the
__width attribute. If the new value is valid, the setter should update the __width
attribute. o height: The getter method should return the __height attribute. Knowing
that __height cannot be negative or 0, the setter should check if client tries to set
an invalid value, if so, the setter should print a meaningful message, and not update
the __height attribute. If the new value is valid, setter should update the __height
attribute.  Three readonly properties: o bottomRight: Returns a Point object
representing the bottom right corner of the Rectangle. This will be calculated using
the topLeft, width and height property values. o area: returns the area of the
rectangle calculated using the width and height property values. o perimeter: returns
the perimeter of the rectangle calculated using the width and height property values. 
A constructor: o This takes three required arguments:  An object of Point class
representing the top-left corner of the rectangle.  the width of the rectangle  the
height of the rectangle Width and height arguments cannot be negative or 0. If either
of them is invalid, the constructor should print a meaningful message. In case of
error, the constructor should set the value of the attribute to the corresponding
static attribute (either DEFAULT_WIDTH or DEFAULT_HEIGHT respectively.) The constructor
should increment the static attribute rectangleCount (which keeps track of the number
of rectangles created) by 1.  One Method: o translate(dx,dy): method just calls the
translate method of the top left point, effectively moving the rectangle by dx in
x-direction and by dy in y-direction. Write both the classes in a single file called
rectangle.py. Now run the provided rectangleClient.py file. It should run without
errors and should give the output as shown in the screenshot of the sample run below.
NOTE: you shouldn’t modify the client code. It just has to run correctly and give
output as shown in the screenshot below. This file has a couple of methods that verify
actual values against expected ones using assert statements. If the check fails,
it will raise an AssertionError exception. You can disable these checking methods by
setting checkAll global variable to False in the client file. Submit the program in a
file with a name first_last_rectangle.py. Make sure to add a block-comment at the start
of the file that lists assignment title, class name, date, your name, and assignment
description. Follow naming conventions."""

# Assignment: DEV128 Rectangle and Point classes
# Class: DEV 128 11065
# Date 4/30/2024
# Author: Rob Ranf
# Description: A Point class and a Rectangle class to represent a point and a
# rectangle in a 2-dimensional coordinate space.


class Point:
    __x: int
    __y: int

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def translate(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy


class Rectangle:
    DEFAULT_WIDTH: int = 1
    DEFAULT_HEIGHT: int = 1
    rectangle_count: int = 0
