import turtle

def line(turtle, level, length):
    if level == 0:
        turtle.forward(length)
    if level != 0:
        line(turtle, level-1, length/4)
        turtle.right(85)
        line(turtle, level-1, length/4)
        turtle.left(170)
        line(turtle, level-1, length/4)
        turtle.right(85)
        line(turtle, level-1, length/4)
def fractal(turtle, deg, length):
    for i in range(4):
        line(turtle, deg, length)
        turtle.right(90)

def main():
    window = turtle.Screen()
    t1 = turtle.Turtle()
    t1.speed('fastest')
    fractal(t1, int(input("What degree do you want the turtle to draw? ")), int(input("And how far? ")))
    t1.end_fill()
    window.exitonclick()
if __name__ == "__main__":
    main()