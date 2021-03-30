'''
File: caesar.py
Authors: Jacob Lane Ledbetter, Jalethzie Pena
Date: March 24, 2021
Description: Program that encrypts a file and returns a file with
the encryption.
'''
def totally_secure(imp, n):#takes the original message and scrambles the message by 'n' characters
    out = ""
    for i in range(len(imp)):
        c = imp[i]
        if (c.isupper()):
            out += chr((ord(c) + n-65) % 26 + 65)
        else:
            out += chr((ord(c) + n - 97) % 26 + 97)
    return out


def main(): #Writes and reads most of the files needed for shifting
    file = input("What is the file name of the text you want to 'secure'? ")

    outfile = open(input("What do you want the out file to be called?"), 'a')

    with open(file, 'r') as openfile:
        imp = openfile.read().replace('\n', '')

    n = int(input("What is the shift?"))

    out = totally_secure(imp, n)

    print("Original Text: ", imp)

    print("The Shift is: ", n)

    print("The cipher is :", out)

    outfile.write(out)

    outfile.close()

    #Boilerplate stuff
if __name__ == "__main__":
    main()