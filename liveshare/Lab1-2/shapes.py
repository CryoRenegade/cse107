# @file shapes.py
# @author Jacob Ledbetter, Jareth Tipton
# @description Does some math for shapes

import math

shape = input("Please enter a shape: ")
if shape == "circle":
    radius = int(input("Please enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    area = math.pi * (radius * radius)
    print("The circumference of the circle is ", circumference)
    print("The area of the circle is ", area)
elif shape == "rectangle":
    length = int(input("Please enter the side length of the rectangle: "))
    width = int(input("Please enter the side width of the rectangle: "))
    perimiter = (length * 2) + (width * 2)
    area = length * width
    print("The perimeter of the rectangle is ", perimiter)
    print("The area of the rectange is ", area)
elif shape == "square":
    length = int(input("Please enter the side length of the square: "))
    perimiter = length * 4
    area = length * length
    print("The perimeter of the square is ", perimiter)
    print("The area of the square is ", area)
else:
    print("Error, valid shapes are: circle, rectangle and square.")
