def read_scores(values):
    """This function takes a list of strings that represent whitespace-separated data.
    Returns a list of dictionaries.
    """
    data = []


        # Creates an empty dictionary
    row = dict()

        # TODO the row dictionary should have 7 keys 
    row["state"] = values(0)
    row["act_percent_taking"] = values(1)
    row["act_average_score"] = values(2)
    row["sat_percent_taking"] = values(3)
    row["sat_average_math"] = values(4)
    row["sat_average_reading"] = values(5)
    row["sat_average_writing"] = values(6)
    print(values)
    data.append(row)

    return data


def test():
    # TODO What if the file doesn't exist? What if the filename is a directory 
    # and not a file? Make sure you catch exceptions when opening this file.
    file = "actsat.txt"
    arr = []
    with open(file, 'r') as openfile:
        f = openfile.read()
        for lines in f:
            arr = arr.append(lines)
            print(arr)
            for data_row in read_scores(arr):
                print(data_row)
    # This is a list of strings.
    print(f)






def main():
    test()

if __name__ == "__main__":
    main()