# Fill in a correct implementation for each function.
# Define other functions if you think they make the
# assigned function easier to write or easier to read.

def all_have_value(lst):
    """
    This function returns True if all list elements have a value other
    than '-', False otherwise.
    """
    for i in lst:
        if i == "-":
            return 0
        else:
            return 1


def all_equal(lst):
    value = all_have_value(lst)
    if value == 0:
        return 0
    else:
        return all(i == lst[0] for i in lst)


def select_row(array, index):
    new_list = array[index]
    return new_list


def select_col(array, index):
    print(array)
    return [row[index] for row in array]

def run_tests():
    """This function tests each function defined in this module."""

    # A single test is a tuple containing the function
    # which is being tested, a sample input, and the correct output.
    # Tests should be written using the unittest or pytest modules,
    # but, hopefully, this code is easier to understand.
    tests = [
        # This test will be used to check if `sum([1, 2, 3])` is `6`.
        (all_have_value, [1, 2, 3, 4, 5], True),
        (all_have_value, ['c', 'a', 't'], True),
        (all_have_value, ['-', '-'], False),
        (all_equal, [1, 1, 1, 1, 1], True),
        (all_equal, ['-', '-'], False),
        (all_equal, ['python', 'python'], True),
        (select_row, [[1,2,3],[4,5,6],[7,8,9]], 1, [4,5,6]),
        (select_row, [[1,1,3],[1,1,4]], 0, [1,1,3]),
        (select_row, [[1], [2], [3], [4]], 3, [4]),
        (select_col, [[1,2,3],[4,5,6],[7,8,9]], 0, [1,4,7]),
        (select_col, [[1,1,3], [1,1,3]], 2, [3,3]),
        #(select_col, [5,4,3,2,1], 3, [2])

    ]


    passed = 0
    failed = 0

    # Test each function.
    # Print a detailed error message whenever a function fails a test.
    for test in tests:
        if len(test) ==  4:
            f = (test[0])
            result = f(test[1], test[2])
            expected = test[3]
            if result == expected:
                passed += 1
            else:
                failed += 1

                # f.__name__ is the function's name
                # for example, select_row.__name__ is the string "select_row"
                print("Function '{}' given arguments {}, {}".format(f.__name__, test[1], test[2]))
                print("Expected {}, but returned {}".format(expected, result))
        else:
            f = (test[0])
            result = f(test[1])
            expected = test[2]
            if result == expected:
                passed += 1
            else:
                failed += 1

                # f.__name__ is the function's name
                # for example, select_row.__name__ is the string "select_row"
                print("Function '{}' given argument {}".format(f.__name__, test[1]))
                print("Expected {}, but returned {}".format(expected, result))
    print("\nPassed {} out of {} tests.".format(passed, passed + failed))


if __name__ == "__main__":
    run_tests()
