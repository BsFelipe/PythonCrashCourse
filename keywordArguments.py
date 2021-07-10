#the current lesson
#keyword arguments = arguments preceded an identifier when we pass them to a function
#                   the order of the arguments doesn't matter, unlike positional arguments
#                   Python knows the names os the arguments thar our function receveis

def hello(first, middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="silva",middle="felipe",first="bug")