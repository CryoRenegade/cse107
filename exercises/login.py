name = "Josh"
password = "Friday"
inputName = 
print("What is your name? ")
input(inputName)
print("Hello ", inputName, "what is the password? ")
input(inputPassword)

if inputName == name:
    print("Whats good my dude, welcome back!")
else:
    if inputName != name:
        print("Nice try tough guy, now get out before the dog smells you...")
    if inputPassword != password:
        print("Who the fuck are you!")
        exit
    else:
        print("You are now logged in!")
