import math
number = float(input("Enter a number to use: "))
choice = input(
    "Which opernation? sqrt (s), arcsin (a), arccos (c), arctan (t):")

if choice == "s":
    if number > 0:
        postnumber = math.sqrt(number)
        print("The square root of the input is ", postnumber)
    else:
        print("The input needs to be a non-negative")
        exit
elif choice == "a":
    if number <= 1 and number >= -1:
        postnumber = math.asin(number)
        print("The arcsin of the input is ", postnumber)
    else:
        print("The input should be between -1 and 1")
        exit
elif choice == "c":
    if number <= 1 and number >= -1:
        postnumber = math.acos(number)
        print("The arccosine of the input is ", postnumber)
    else:
        print("The input should be between -1 and 1")
        exit
elif choice == "t":
    postnumber = math.atan(number)
    print("The arctangent of the input is ", postnumber)
