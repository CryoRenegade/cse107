import turtle

def draw_cesaro_line(turtle, level, length):
    if level == 0:
        turtle.forward(length)
    if level != 0:
        draw_cesaro_line(turtle, level-1, length/4)
        turtle.right(85)
        draw_cesaro_line(turtle, level-1, length/4)
        turtle.left(170)
        draw_cesaro_line(turtle, level-1, length/4)
        turtle.right(85)
        draw_cesaro_line(turtle, level-1, length/4)
def draw_cesaro_fractal(turtle, level, length):
    for i in range(50):
        draw_cesaro_line(turtle, level, length)
        turtle.right(90)

def main():
    window = turtle.Screen()
    t1 = turtle.Turtle()
    t1.speed('fastest')
    t1.begin_fill()
    draw_cesaro_fractal(t1, 3, 2000)
    t1.end_fill()
if __name__ == "__main__":
    main()