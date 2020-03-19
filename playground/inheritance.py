class Predator:
    def eating(self):
        print('I want meat!!!')

class Wolf(Predator):
    def eating(self):
        print('I am Wolf! And i want to eat sheep!!!')

class Kenguru:
    def eating(self):
        print('I am Kenguru! And i want to eat green trees!!!')

class Dog(Wolf, Kenguru):
    def eating(self):
        super(Wolf, self).eating()
        Predator.eating(self)
        #print('I am dog! And i want to eat meat!!!')

dog = Dog()
print(Dog.mro())
dog.eating()