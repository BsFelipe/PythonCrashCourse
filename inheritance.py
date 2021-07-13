#We can use a parent class where its children can inherit its attributes and methods
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is runnig")
class Fish(Animal):
    def swin(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

