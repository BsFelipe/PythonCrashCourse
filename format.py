# str.format() = optional method that gives users
#		 more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item) not elegant

#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item))#positional argument
#print("the {item} jumped over the {animal}".format(animal="cow",item="moon"))#keyword argument

text = "The {} jumped over the {}"
#print(text.format(animal,item))

name = "Felipe"

#print("Hello, my name is {}. Nice to meet you".format(name))
#print("Hello, my name is {:10}. Nice to meet you".format(name))#:10 padding
#print("Hello, my name is {:<10}. Nice to meet you".format(name)) # padding after the placeholder
#print("Hello, my name is {:>10}. Nice to meet you".format(name)) # padding before the placeholder
#print("Hello, my name is {:^10}. Nice to meet you".format(name)) # padding center the placeholder

n1 = 3.14159
n2 = 1000

print("The number pi is {:.2f}".format(n1))
print("The number is {:,}".format(n2))
print("The number is {:b}".format(n2)) #binary
print("The numer is {:o}".format(n2)) #octal, base-8
print("The numer is {:X}".format(n2)) #hexadecimal
print("The numer is {:e}".format(n2)) #scientific notation