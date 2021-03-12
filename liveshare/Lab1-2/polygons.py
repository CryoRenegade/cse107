import turtle

t1 = turtle.Turtle()
length = float(input("Please Enter A Length for all sides: "))

for i in range(3):
    t1.left(120)
    t1.forward(length)
t1.forward(150)

for i in range(4):
    t1.left(90)
    t1.forward(length)
t1.forward(150)
for i in range(5):
    t1.left(72)
    t1.forward(length)
t1.forward(200)

for i in range(6):
    t1.left(60)
    t1.forward(length)
t1.forward(250)

for i in range(7):
    t1.left(51.43)
    t1.forward(length)
