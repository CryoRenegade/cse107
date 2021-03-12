#Does a luhns calculation on the numbers that are inputted into the console.
def validate(cardNo):
    count = len(cardNo)
    s = 0
    IsItASecond = False
    for i in range(count - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (IsItASecond == True):
            d = d * 2
        # We add two digits to handle cases that make two digits after doubling
        s += d // 10
        s += d % 10
        IsItASecond = not IsItASecond
    if (s % 10 == 0):
        return True
    else:
        return False
#Calls the validate function and prints the output after calculation
def main():
    cardNo = input("What card number do you want to validate?")
    if (validate(cardNo)):
        print("This is a valid card")
    else:
        print("This is not a valid card")
#Boilerplate
if __name__ == "__main__":
    main()