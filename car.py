#objects = get a object (tangible or not) for the real world and model in the computer world
#attributes = is/has , describe the object. Who it's like, traits an etc (name, height, color)
#methods = actions that the object do. (ex: run, sleep, jump)

class Car:

    wheels = 4 #class variable..a variable default of the class

    def __init__(self, make,model,year,color): #especial method, construct the object for us (constructor)
        # attributes
        self.make = make #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable

    #methods
    def drive(self):
        print("this "+self.model+" is driving")
    def stop(self):
        print("this "+self.model+" is stopped")

