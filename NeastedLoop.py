#the "inner loop" will finish all of it's interations before finishing one interation of the "outer loop"

rowns = int(input("how many rows?: "))
collumns = int(input("how many collums?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rowns):
    for j in range(collumns):
        print(symbol, end="")
    print(".")
