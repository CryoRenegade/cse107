"""
Finds the minimum, maximum, sum, midpoint, average, and the ability to search
of/in an array of any size, which is entered by the user.

file: listFunctions.py
authors: Jacob Ledbetter and Maya Savino
date: 17 February 2021
assignment: Prelab 3
"""


"""Used for some maths that we couldnt be bothered with"""


import statistics
"Defines a function for finding the max number in a given array"


def max(values):
    final = int((len(values) - 1))
    maximum = values[final]
    return maximum


"Defines a function to find the minimum number in a given array"


def min(values):
    minimum = values[0]
    return minimum


"Defines a function that finds the total sum of a given array"


def sum(values):
    sum1 = int(math.fsum(values))
    return sum1


"Defines a function that finds the median of a given array"


def midpoint(values):
    midpoint = statistics.median(values)
    return midpoint


"Defines a function that finds an given integer in a given array"


def linear_search(values):
    n = int(input("Enter the integer that you want to search for: "))
    for i in range(len(values)):
        if values[i] == n:
            return (i, True)


"Defines a function that finds the mean of a given array"


def average1(values):
    aver = statistics.mean(values)
    return aver


"Defines a function that reverses the order of a given array"


def reverse(values):
    values.sort(reverse=True)
    return values


"Defines the main function of our code that gives the users the ability to input an array and do various functions with it"


def main():
    stop = ""
    values = []
    "Defines a loop for users to input an array over and over again until they say yes to stop the loop"
    while stop != "yes":
        t = int(input("Enter a number for the array: "))
        values.append(t)
        stop = input("Do you want to stop? ")
        stop = stop.lower()
    choice = ""
    "Defines a loop that takes a users choice and runs the function that is correlated to the input"
    while choice != "stop":
        choice = input(
            "What do you want to do with the array? Type list for a list of operations. Type stop to stop: ")
        "sanitizes all inputs to make them compatible (and to save my sanity)"
        choice = choice.lower()
        values.sort()
        if choice == "max":
            maximum = max(values)
            print("Maximum:", maximum)
        elif choice == "min":
            minimum = min(values)
            print(minimum)
        elif choice == "sum":
            sumfin = sum(values)
            print(sumfin)
        elif choice == "midpoint":
            mid = midpoint(values)
            print(mid)
        elif choice == "linear_search":
            n = linear_search(values)
            print(n)
        elif choice == "average":
            aver = average1(values)
            print(aver)
        elif choice == "reverse":
            rev = reverse(values)
            print(rev)
        "Gives a list of all possible functions"
        elif choice == "list":
            print("The operations that are currently supported are: Max, Min, Sum, Midpoint, Linear_Search, Average, Reverse: ")
        else:
            print(
                "That isnt a supported function, you can either 1. Go to school, or 2. type list: ")
    exit()


"Main Boilerplate code for main function"
if __name__ == "__main__":
    main()
