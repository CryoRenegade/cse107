"""
This test assumes your function is named `count_letters`.
This function must take a string and return a dictionary.
"""

import lettercount

test_cases = [("", dict()),
              ("abc", {'a': 1, 'c': 1, 'b': 1}),
              ("ABC abc", {'a': 2, 'c': 2, 'b': 2}),
              ("The cat in the hat",
               {'h': 3, 'i': 1, 'c': 1, 't': 4, 'n': 1, 'a': 2, 'e': 2}),
              ("A partial solar eclipse will occur on August Third",
               {'h': 1, 'c': 3, 'o': 3, 'w': 1, 'n': 1, 't': 3, 'd': 1,
                'l': 5, 'i': 4, 'p': 2, 'g': 1, 'r': 4, 'a': 5, 's': 3,
                'u': 3, 'e': 2}
              )]

def test_lettercount():
    passed = 0
    for test, result in test_cases:
        output = lettercount.count_letters(test)
        if output != result:
            print("input '{}' should return\n{}\nbut returned\n{}".format(
                test, result, output))
        else:
            passed += 1
    print('passed {} out of {} tests'.format(passed, len(test_cases)))

if __name__ == '__main__':
    test_lettercount()
