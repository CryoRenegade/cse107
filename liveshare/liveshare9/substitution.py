'''
File: substitution.py
Authors: Jacob Lane Ledbetter, Jalethzie Pena
Date: March 24, 2021
Description: Program that can encrypt and decrypt files
using the substitution method.
'''

import random
def encrypt(key, abc):
    ### asks user the file they need encrypted and uses a randomly generated
    ### alphabet to change the letters in a file to new letters.
    file = input("What is the file name of the text you want to 'scramble'? ")

    with open(file, 'r') as openfile:
        imp = openfile.read().replace('\n', '')
    map = dict(zip(abc, key))
    return ''.join(map.get(c.lower(), c) for c in imp)

def decrypt(key, abc): #Asks user the file they need decrypted and uses a randomly generated alphabet
    #to decode the message in a file return the decrypted message.
    file = input("What is the file name of the text you want to 'descramble'? ")

    with open(file, 'r') as openfile:
        imp = openfile.read().replace('\n', '')
    map = dict(zip(key, abc))
    return ''.join(map.get(c.lower(), c) for c in imp)

def abc_scramble(abc): #Makes scrambled eggs out of the alphabet
    abc = list(abc)
    random.shuffle(abc)
    return ''.join(abc)

def main():
    abc = 'abcdefghijklmnopqrstuvwxyz.,! ' #The OG ABC's

    choice = input("Do you want to encrypt or decrypt the file? ")

    if choice == "encrypt" or choice == "Encrypt": #We have to make a hard choice here
        key = abc_scramble(abc)
        outfile = open(input("Where do you want to store the key? "), 'a')
        outfile.write(key)
        outfile.close()
        out = encrypt(key, abc)
        print(out)
        afterfile = open(input("What do you want the out file to be called? "), 'a')
        afterfile.write(out)
        afterfile.close()
    elif choice == "decrypt" or choice == "Decrypt":
        file = input("Where is the key to the WiFi grandma? I wanna play fortnite!!! ")
        with open(file, 'r') as openfile:
            key = openfile.read().replace('\n', '')
        out = decrypt(key, abc)
        print(out)
        afterfile = open(input("What do you want the out file to be called? "), 'a')
        afterfile.write(out)
        afterfile.close()
    else: #A quote i got from google.
        print("Just admit you screwed up, and take whatever steps you need to take to rectify it. Apologize for what happened, ensure to people that it won't happen again. - William Forsyth")
        exit
        #Boilerplate stuffs
if __name__ == "__main__":
    main()