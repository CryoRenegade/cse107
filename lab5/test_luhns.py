"""
This test assumes your functions are named as follows:
    validate: Take in a credit card number as a string and return True if valid, False if no.

You should make no other changes to this file.
"""

import luhns  # Make sure test_luhns and luhns.py are in the same directory.


def main():
    # This is a list of tuples, the first element is a card number
    # and the second is a boolean that's True if the card number is
    # valid and False if it is not.
    test_cases = [("38520000023237", True),
                  ("49927398716", True),
                  ("49927398717", False),
                  ("1234567812345678", False),
                  ("1234567812345670", True)]

    passed = 0
    for card_number, expected_result in test_cases:
        result = luhns.validate(card_number)
        if expected_result == result:
            passed += 1
        else:
            print('luhns.validate("{}") should return {}, but returned {}.'.format(card_number, expected_result, result))

    print('The function luhns.validate correctly verified ' + '{} out of {} card numbers.'.format(passed, len(test_cases)))


if __name__ == '__main__':
    main()
