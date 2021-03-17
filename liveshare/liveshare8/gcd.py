# Jacob Ledbetter & Johnny Raymond
# This program solves for the greatest common divisor given two user inputs

def gcd(a, b): # This definition solves for the gcd of x and y in the main() using a and b.
    for i in range(a):
        if (a == 0):
            return b
        else:
            q = a % b
            b = a
            a = q

def main(): # Takes user defined variables and sets it to x and y, then calls on gcd()
    x = int(input("Please enter an integer: "))
    y = int(input("Please enter another integer: "))
    print("The greatest common devisor of", x, "and", y, "is", gcd(x, y))

#Boilerplate code for beauty and stuffs.
if __name__ == "__main__":
    main()