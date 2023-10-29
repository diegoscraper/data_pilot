"""
Keyword arguments are a way to pass arguments to a function using
their parameter names. This allows us to pass arguments in any
order, as long as we specify the parameter names.
"""


def subtract_numbers(x, y):
    return x - y


result = subtract_numbers(y=3, x=10)

print(result)
