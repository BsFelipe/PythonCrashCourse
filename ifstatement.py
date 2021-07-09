#IF statements > in block of code if that condition is true, the block will execute
"""
age = int(input("How old are you?: "))

if age == 100:
    print("You are an older")
elif age > 26:
    print("You are an adult")
elif age > 18:
    print("You're a adult tenneger")
elif age > 14:
    print("You are a tenneger")
else:
    print("You are an child")
"""
#logical operator (and,or,not) = is used to check if one or more condition is true

temper = int(input("What is the temperature outside? "))

if not(temper >= 16 and temper < 26): #NOT operator reverse the result of the condition..if is normaly true, become not true. If false, become true.
    print("the temperature is good today!")
    print("go outside!")
elif temper < 16 and temper > 12:
    print("A little cold, but you can go outside")

elif temper < 12:
    print("The temperature is cold, but if you like..")
else:
    print("Is hot...")




