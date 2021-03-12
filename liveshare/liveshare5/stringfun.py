
def ends(end):
    number = 0
    for i in end:
        number = number + 1
    first_last = end[0:2] + end[number - 2: number]
    return first_last


def mix(s1, s2):
    mixed_1 = s2[:2] + s1[2:]
    mixed_2 = s1[:2] + s2[2:]
    return mixed_1, mixed_2


def main():
    choice = ""
    while choice != "stop":
        choice = input(
            "What do you want to do with the strings? Either end or mix, not both. Type stop to stop: ")
        if choice == "end":
            user_input = (input("Enter a string: "))
            x = ends(user_input)
            print(x)
        elif choice == "mix":
            x = input("Enter a string: ")
            y = input("Enter another string: ")
            x = mix(x, y)
            print(x)
        else:
            print("Huh, what in the name of Schwarzenegger did you type?")


if __name__ == "__main__":
    main()
