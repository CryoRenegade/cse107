import math
def split(arr):
    return [char for char in arr]

def get_number_of_args(func):
    """ Computes the number of arguments of a given function.

    :returns: number of arguments of a given function
    :rtype: int
    """
    variables = list(func.__code__.co_varnames)
    return len(variables)

def func_sum(a,b):
    """ Computes the sum between the two variables.

    :returns: sum between a and b
    :rtype: int
    """
    return a + b

def func_sub(a,b):
    """ Computes the subtraction between the two variables.

    :returns: subtraction between a and b
    :rtype: int
    """
    return a - b

def func_mul(a,b):
    """ Computes the multiplication between the two variables.

    :returns: multiplication between a and b
    :rtype: int
    """
    return a * b

def func_div(a,b):
    """ Computes the division between the two variables.

    :returns: division between a and b
    :rtype: int
    """
    return float(a) / b

def func_sqrt(a):
    """ Computes the square root of a.

    :returns: square root of a
    :rtype: int
    """
    return math.sqrt(a)

# Mapping between the operator and the function that calculates the result


def main():
    """ Computes the result of the expression in arr.

    :returns: None
    """
    operators = {
        '+': func_sum,
        '-': func_sub,
        '*': func_mul,
        '/': func_div,
        'sqrt': func_sqrt
        }
    arr = input("Please enter an equation")
    arr = split(arr)
    arr_copy = arr[:]
    i = 0
    while len(arr) != 1:
        if isinstance(arr[i], str):
            op = arr[i]
            num = get_number_of_args(operators[op])
            res = operators[op]/(arr[i-num:i])
            arr[i-num] = res
            if num == 2:
                f=arr.pop(i-num+1)
                s=arr.pop(i-num+1)
            if num == 1:
                f=arr.pop(i-num+1)
            i -= num
        else:
            i += 1
    print("The result of", arr_copy, "is:", arr[0])

if __name__ == "__main__":
    main()