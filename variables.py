##WORKING WITH VAR
print("String Type")
first_name = 'felipe'
last_name = 'belo' #in python is a good semantic use _ in variable
full_name = first_name + ' ' + last_name
print(full_name)
print(type(full_name))
print("################")

print("Integer type")
##integer
age = 28
age += 1
#in py you can't concatenate differents types of VAR
print("Yor age is " + str(age))
print(type(age))
print('################')

print("Float Type")
#float
height = 181.5
print("Your height is: " + str(height) + "cm")
print(type(height))
print("################")

print("Boolean Type")
#boolean
human = True #py is case sentive
print("Are you a human: " + str(human))
print(type(human))

#Multiple assignment > in py you can make multipe assignments

#name = 'Felipe'
#age = 28
#attractive = True

#the example bellow is the same
#name, age, attractive = "felipe", 29, True

#And so, you can assignment one value to multiple variables
#Age_Felipe = 29
#Age_Joao = 29
#Age_Jose = 29
#Age_Benjamin = 29
#Age_Felipe = Age_Joao = Age_Jose = Age_Benjamin = 29