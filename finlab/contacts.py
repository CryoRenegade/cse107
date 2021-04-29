import csv
def info(rows):
    None
def lists(choice):
    with open(choice, 'r') as page:
        print(page.read())
def load(row):
    choice = input("What file would you like to load? If you want the default file, just enter contacts.csv. ")
    with open(choice, 'r') as page:
        reader = csv.reader(page, delimiter = '\t')
        for row in reader:
            row.append(reader)
            print(row)
        return(row)
def add(row):
    stuff = [input("What is the name of the contact?"), input("What is their phone number?"), input("What companmy do they work for?"), input("What is their email?"), input("Any Notes?")]
    row.append(stuff)
    return(row)
def note():
    None
def remove():
    None
def save(row):
    choice = input("What file would you like to load? If you want the default file included with the package, just enter contacts.csv. ")
    with open(choice, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(row)
def commandme():
    None
def main():
    row = []
    print("Welcome to Cryo's Contact Contract Purgatory! To know more about this app, use the about command!")
    while True:
        command = input("What command would you like to run?: ")
        if command == "about" or command == "About":
            with open('README.md', "r") as openfile:
                print(openfile.read())
        elif command == "exit" or command == "Exit":
            print("Hasta la vista or whatever, i don't care (baka...). Come back soon!")
            exit()
        elif command == "info" or command == "Info":
            info(page)
        elif command == "list" or command == "List":
            lists(page)
        elif command == "load" or command == "Load":
            page = load(row)
        elif command == "add" or command == "Add":
            add(page)
        elif command == "note" or command == "Note":
            note(page)
        elif command == "remove" or command == "Remove":
            remove(page)
        elif command == "save" or command == "Save":
            save(page)
        elif command == "commands" or command == "Commands":
            commandme(page)
if __name__ == "__main__":
    main()