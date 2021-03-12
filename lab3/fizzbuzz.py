import math


def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("{}".format(i), end=" ")
        return "FizzBuzz"


def fizz(i):
    if i % 3 == 0:
        print("{}".format(i), end=" ")
        print("Fizz")


def buzz(i):
    if i % 5 == 0:
        print("{}".format(i), end=" ")
        print("Buzz")
    elif i % 3 and i % 5 != 0:
        print("{}".format(i))


def main():
    i = 1
    number = int(input("Enter a number:"))
    if number >= 0:
        while i <= number:
            o = fizzbuzz(i)
            if o == "FizzBuzz":
                print(o)
            else:
                fizz(i)
                buzz(i)
            i = i + 1
    else:
        print("Not a positive number!")


if __name__ == "__main__":
    main()
