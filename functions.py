#function = a block of code which is executed only when it is called

def hello(first_name,last_name,age):
    print("hello "+first_name+" "+last_name)
    print("You are " +str(age)+" years old")

my_name = "Felipe"
last_name = "Silva"
age = 28

hello(my_name,last_name,age)