try:
    with open('test.tt') as file: #open and close file automatically
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

#print(file.closed)