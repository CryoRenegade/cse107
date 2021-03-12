choice = int(
    input("(1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker):)"))
if choice == 1:
    salary = int(input("Enter weekly salary:"))
    print("The manager's pay is ", salary)
elif choice == 2:
    salary = int(input("Enter the hourly salary: "))
    hours = float(input("Enter total hours worked: "))
    if hours > 40:
        overtime = hours - 40
        hours = hours - overtime
        regpay = hours * salary
        overpay = overtime * (salary * 1.5)
        pay = overpay + regpay
        print("The worker's pay is ", pay)
    elif hours < 40:
        pay = hours * salary
        print("The worker's pay is ", pay)
elif choice == 3:
    sales = int(input("Enter gross weekly sales: "))
    pay = 250
    postsales = sales * 0.057
    pay = postsales + pay
    print("The commision worker's pay is ", pay)
elif choice == 4:
    pieces = int(input("Enter number of peices made:"))
    wage = int(input("Enter the wage per peice:"))
    pay = pieces * wage
    print("The peice worker's pay is", pay)
else:
    print("Error, the given employee code is not valid.\n Valid codes are:\n 1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker")
