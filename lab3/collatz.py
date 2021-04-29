
"""Initialize the function for the collatz math"""


def collatz_len(c):
    count = 1
    if c == -1:
        print("There is no way in hell that is happening, denied.")
        exit()
    while c != 1:
        if c % 2 == 0:
            c = c / 2
        else:
            c = (c*3) + 1
        count = count + 1
    return count


"""Initialize the main function to call other functions for the collatz math to get the inputted number down to one."""


def main():
    c = int(input("Enter a starting number:"))
    if c == -1:
        print("There is no way in hell that is happening, denied.")
        exit()
    count = collatz_len(c)
    print("Length of Collatz sequence:", count)


"""Boilerplate for main function"""
if __name__ == "__main__":
    main()
