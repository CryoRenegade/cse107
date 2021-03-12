def lowest(num, den):
    # Finding gcd of both terms
    common_factor = gcd(num, den)
    # Converting both terms into simpler terms by dividing them by common factor
    den = int(den / common_factor)
    num = int(num / common_factor)
    return (num, den)
#Greatest Common Denominator code
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def add(num1, den1, num2, den2):
    # Finding gcd of den1 and den2
    den3 = gcd(den1, den2)
    # Denominator of final fraction obtained finding LCM of den1 and den2 LCM * GCD = a * b
    den3 = (den1 * den2) / den3
    # Changing the fractions to have same denominator Numerator of the final fraction obtained
    num3 = ((num1) * (den3 / den1) + (num2) * (den3 / den2))
    # Calling function to convert final fraction into it's simplest form
    lowest(den3, num3)
    return (num3, den3)
#Multiplies the fractions
def multiply(frac1, frac2):
    dev1 = (frac1[0] * frac1[1])
    dev2 = (frac2[0] * frac2[1])
    return (dev1, dev2)
#Divides the fractions
def divide(frac1, frac2):
    dev1 = (frac1[0] * frac2[1])
    dev2 = (frac1[1] * frac2[0])
    return (dev1, dev2)
#Asks for input and computes fractions
def main():
    frac1 = (float(input("What is the numerator? ")) ,float(input("What is the denominator? ")))
    frac2 = (float(input("What is the numerator of the second fraction?")) ,float(input("What is the denominator? ")))
    redfrac1 = lowest(frac1[0], frac1[1])
    redfrac2 = lowest(frac2[0], frac2[1])
    print("Reduced fractions to", redfrac1, " ", redfrac2)
    print("Sum of the fractions: ", add(redfrac1[0], redfrac1[1], redfrac2[0], redfrac2[1]))
    print("Multiplication of the fractions: ", multiply(frac1, frac2))
    print("Division of the first by the second: ", divide(frac1, frac2))

#Boilerplate
if __name__ == "__main__":
    main()