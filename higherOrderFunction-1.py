# Higher order function = a function that either:
#                         1. accepts a function as an argument
#                            or
#                         2. returns a function
#                         (In Python, functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(quiet)
