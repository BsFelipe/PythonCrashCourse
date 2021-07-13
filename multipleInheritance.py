#multiple inheritance = when a child class i derived from more than one parent class

class Prey:
    def flee(self):
        print("this animal fless")

class Predator:
    def hunt(self):
        print("this animal is hunting")

class Raabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Raabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()

