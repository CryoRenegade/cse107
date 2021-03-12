ammount = int(input("Please enter a dollar ammount: "))
bills = [20, 10, 5, 1]
amountafter = [0, 0, 0, 0]

for a, b in (bills, amountafter):
    if ammount >= a:
        b = ammount // a
        ammount = ammount - b * a
        print(a, " : ", b)
