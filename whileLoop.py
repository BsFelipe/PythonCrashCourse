#while loop = a statement that will execute a block of code,
# until that condition remains true

""""
name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)
"""

name = None

while not name: #while name is empty, do
    name = input("Enter your name: ")
print("Hello " + name)

