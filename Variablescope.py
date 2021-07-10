# scope = the region that a variable is recognized
#          A variable is only avaiable from inside the region it is created
#           A global and locally scopped versions of a variable can be crated

name = "Bro" #global scope (avaible inside & outside functions)

def display_name():
    name = "code" #local scope (available only inside this function)
    print(name)

display_name()
print(name)

#Python Scope & the LEGB Rule
#L = Local
#E = enclosing
#G = Global
#B = built-in