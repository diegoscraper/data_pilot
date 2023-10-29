"""
Variable-length arguments allow a function to accept an arbitrary
number of arguments. There are two types of variable-length
arguments in Python:
*args: This allows a function to accept an arbitrary number of
positional arguments.
**kwargs: This allows a function to accept an arbitrary number of
keyword arguments.
"""


def multiply_numbers(*args):
    result = 1
    for arg in args:
        result *= arg

    return result


result = multiply_numbers(2, 3, 4)
print(result)