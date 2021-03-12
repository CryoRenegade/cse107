total = 0
count = 0
average = 0

for i in range(10):
    count = count + 1
    userinput = int(input("Type a number!"))
    total = total + userinput
    average = total / count
    print(average)
