# *args = parameter that will pack all arguments into a tuple
#	  useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)#its impossible to change value inside a tuple, you need to use a list
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2))
