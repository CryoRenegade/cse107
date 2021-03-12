gradestotal = 0
numberof = int(
    input("Please enter how many grades you would like to include: "))
finalnumberof = numberof
while numberof >= 1:
    grades = input("Please enter student's grade: ")
    if grades == "a" or grades == "A":
        gradestotal = gradestotal + 4
    elif grades == "b" or grades == "B":
        gradestotal = gradestotal + 3
    elif grades == "c" or grades == "C":
        gradestotal = gradestotal + 2
    elif grades == "d" or grades == "D":
        gradestotal = gradestotal + 1
    elif grades == "f" or grades == "F":
        gradestotal = gradestotal + 0
    else:
        print("Please enter a valid letter grade")
        exit
    numberof = numberof - 1
average = int(gradestotal / finalnumberof)
if 0 < average < 1:
    print("The average grade is an F")
elif 1 <= average < 2:
    print("The average grade is a D")
elif 2 <= average < 3:
    print("The average grade is a C")
elif 3 <= average < 4:
    print("The average grade is a B")
elif average == 4:
    print("The average of the class is an A")
else:
    average == 0
    print("What kind of drugs are you on? I want some.")
