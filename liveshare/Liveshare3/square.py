import math
eq = 0
count = int(input("Please enter a positive integer: "))
number = 0
if count < 4:
    print("You cant have anything under four, unless you want to break what we have left of our sanity")
else:
    while count >= eq:
        eq = (number + 2) ** 2
        number = number + 2
        valid = int(eq / count)
        if eq < count:
            print(eq)
exit
