import string
def wordcount(words, d):
    for lines in words:
        lines = lines.strip()
        lines = lines.lower()
        table = str.maketrans(dict.fromkeys(string.punctuation))
        lines = lines.translate(table)
        fin = lines.split(" ")

        for i in fin:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
    return d

def main():
    filename = input("What file would you like to read? ")
    try:
        words = open(filename, "r")
    except FileNotFoundError:
        print('File "{}" not found'.format(filename))
        exit
    except IsADirectoryError:
        print('File "{}" is a directory'.format(filename))
        exit
    except UnboundLocalError:
        exit
    d = dict()
    d = wordcount(words, d)
    choice = input("What word are ya lookin for chief? ")
    try:
        print(choice, ":", d[choice])
    except KeyError:
        print("That ain't in there chief... are you blind or just a fool? No free lunch.")
if __name__ == "__main__":
    main()
