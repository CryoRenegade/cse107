# Prelab 10 - 4.2 Sieve.py
# Gabriel Maestas and Jacob Ledbetter
# 03/31/2021
# Write a program that utilizes regular expression to make sure the password string it is given is strong.
# A strong password is defined as one that is at least eight characters long, contains both upper
# and lowercase characters, and contains at least one digit.


import re
def checkmeout(passw):
    """This function determines if an input password is considered strong or not"""
    lengtherr = len(passw) < 8
    lookfordigit = re.search(r"\d", passw) is None
    uppercaseerr = re.search(r"[A-Z]", passw) is None
    lowercaseerr = re.search(r"[a-z]", passw) is None
    symerr = re.search(r"\W", passw) is None

    passok = not (lengtherr or lookfordigit or uppercaseerr or lowercaseerr or symerr)
    return passok

def main():
    passw = input('Please input a password to test: ')
    ans  = checkmeout(passw)
    print("The password is: ", ans)
if __name__ == '__main__':
    main()