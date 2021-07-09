#Loop Control = change a loops execution from its normal sequence

#break = teminate the loop
#continue = skip to the next iteration of the loop
#pass = does nothing, acts as placeholder

#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

phone_number = "+55-11-94954-65-11"

#for i in phone_number:
    #if i == "-" or i == "+":
        #continue
#    print(i,end="")

for i in range(1,20):
    if i == 9:
        pass
    else:
        print(i)