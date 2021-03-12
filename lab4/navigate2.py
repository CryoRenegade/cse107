"""imports important package for our program"""
import turtle
"""Implement the turtle by name t1"""
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


"""Implements main code execution"""


def main():
    """Initializes the choice variable for the while function"""
    choice = []
    nums = []
    choice.append(input("Please enter a direction:"))
    """Makes sure the code doesn't stop until the user says STOP, remember kids, you need concent before messing with their code"""
    while choice[-1] != "stop":
        """Inputs user's choice"""
        nums.append(input("Please enter a number for your function"))
        choice.append(input("Please enter a direction:"))
        """Interprets user choice so that invalid choices are nullified"""
    for i in choice:
        n = nums[0]
        if i == "left" or choice == "forward" or choice == "right":
            """Calls the left function with the angel that the user wants"""
            if i == "left":
                left(n)
                nums.pop(0)
#Same as left, but right... right?
            elif i == "right":
                right(n)
                nums.pop(0)
#Moves the turtle forward... somehow?
            elif i == "forward":
                forward(n)
                nums.pop(0)
            #Stops the turtle from destroying the world
        elif i == "stop":
            print("Have a good day!")
            exit
        else:
            print("No valid inputs, learn the program before i sic a terminator on you...")


"""Boilerplate stuff for main function"""
if __name__ == "__main__":
    main()
