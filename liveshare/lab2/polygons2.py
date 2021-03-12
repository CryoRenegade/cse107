import turtle
t1 = turtle.Turtle()

sides = int(input("Please enter the number of sides: "))
length = float(input("Please enter the side-length: "))
degree = 360 / sides

for i in range(sides):
    t1.forward(length)
    t1.left(degree)
