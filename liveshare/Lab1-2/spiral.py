import turtle
t1 = turtle.Turtle()
angle = int(input("Please enter an angle:"))
length = 10
for i in range(128):
    t1.forward(length)
    length = length + 2
    t1.left(angle)
