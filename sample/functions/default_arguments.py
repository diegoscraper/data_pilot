"""
Default arguments are a way to specify a default value for a function
parameter. If the argument is not passed when the function is called,
the default value is used instead.
"""


def greet(name, greeting = "hello"):
    print(f"{greeting}, {name}")


greet("diego")
greet("mary", "hey you")