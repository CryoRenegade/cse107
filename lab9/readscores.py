def read_scores(lines):
    """This function takes a list of strings that represent whitespace-separated data.
    Returns a list of dictionaries.
    """
    data = []

    for line in lines:
        values = line.split()

        # Creates an empty dictionary
        row = dict()

        # TODO the row dictionary should have 7 keys 
        # row["state"] = ...
        data.append(row)

    return data


def test():
    # TODO This should be a with-statement.
    # TODO What if the file doesn't exist? What if the filename is a directory 
    # and not a file? Make sure you catch exceptions when opening this file.
    f = open("actsat.txt")

    # This is a list of strings.
    lines = f.readlines()

    # TODO remove this after adding a with-statement
    f.close()

    for data_row in read_scores(lines):
        print(data_row)


# TODO call the test() function
