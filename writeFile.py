text = "Have a nice day!"

#with open('test.txt','w') as file: #'w' overwriting the file
#    file.write(text)

with open('test.txt','a') as file: # append the file
    file.write(text)