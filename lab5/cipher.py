#Reverses the string
def encrypt(text):
    i = len(text) - 1
    translated = ""
    while i >= 0:
        translated = translated + text[i]
        i = i - 1
    return translated
#Calls the function and outputs the calculation
def main():
    text = input("What string would you like to encode?")
    print("Your encrypted cipher is", encrypt(text))
#Boilerplate
if __name__ == "__main__":
    main()