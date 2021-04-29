"""Grabs code from other program"""
from collatz import collatz_len

"""Defines Function to use code"""


def main():
    countfin = 0
    ifin = 0
    """Runs all numbers between 1 and 1 million to find best collatz score"""
    for i in range(-1000000, 1000000):
        count = collatz_len(i)
        if countfin < count:
            """Fin means final"""
            countfin = count
            ifin = i
    """Print out the options made by the function"""
    print("Longest chain is produced by", ifin,
          "with a sequence of length", countfin)


""" Boilerplate stuff for consistency"""
if __name__ == "__main__":
    main()
