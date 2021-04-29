"""imports important package for our program"""
import turtle
"""Implement the turltle by name t1"""
t1 = turtle.Turtle()

"""Define the function of turning the turtle left"""


def left(angle):
    t1.left(angle)


"""Defines the function of turning the turtle right"""


def right(angle):
    t1.right(angle)


"""Defines the function of moving the turtle forward"""


def forward(length):
    t1.forward(length)


#Implements main code execution


def main():
    """Initializes the choice variable for the while function"""
    choice = ""
    """Makes sure the code doesnt stop until the user says STOP, remember kids, you need concent before messing with their code"""
    while choice != "stop":
        """Inputs user's choice"""
        choice = input("Please enter a direction:")
        """Interperts user choice so that invalid choices are nullified"""
        if choice == "left" or choice == "forward" or choice == "right":
            """Calls the left function with the angel that the usder wants"""
            if choice == "left":
                angle = int(input("How many degrees?"))
                left(angle)
            """Same as left, but right... right?"""
            elif choice == "right":
                angle = int(input("How many degrees?"))
                right(angle)
            """Moves the turtle forward... somehow?"""
            elif choice == "forward":
                length = int(input("How far do you want to go?"))
                forward(length)
        """Stops the turtle from destroying the world"""
        elif choice == "stop":
            print("Have a good day!")
            exit


"""Boilerplate stuff for main function"""
if __name__ == "__main__":
    main()
