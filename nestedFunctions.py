#nested functions calls = function calls inside other function calls
#                         innermost functions calls are resolved first
#                         returned value is used as argument for the next outer function

#more work hard
#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#just one line
print(round(abs(float(input("Enter a whole positive number: ")))))