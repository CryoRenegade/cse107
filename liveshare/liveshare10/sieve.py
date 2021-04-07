# Prelab 10 - 4.2 Sieve.py
# Gabriel Maestas and Jacob Ledbetter
# 03/31/2021
# Write a program that prompts the user for an integer n. The program takes the given integer n
# and uses the sieve algorithm to find all the primes integers less than or equal to n.


def sieve(n):
    """This function finds the prime numbers below and equal to input number"""
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <=n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False
    for p in range(n+1):
        if prime[p]:
            print(p)



def main():
    n = int(input('Please input a number: '))
    sieve(n)
if __name__ == '__main__':
    main()