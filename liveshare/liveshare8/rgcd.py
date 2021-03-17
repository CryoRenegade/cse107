# Jacob Ledbetter and Johnny Raymond
# This program solves for the greatest common divisor given two user inputs

def gcd(n, m):  # This definition solves for the gcd of x and y from main() using m and n. This method uses recursion in the return function.
    if (n == 0):
        return m
    return gcd(m % n, n)

def main(): # Takes user defined variables and sets it to x and y, then calls on gcd().
    x = int(input("Please enter an integer: "))
    y = int(input("Please enter another integer: "))
    print("The greatest common devisor of", x, "and", y, "is", gcd(x, y))

#Boilerplate code for beauty and stuffs.
if __name__ == "__main__":
    main()