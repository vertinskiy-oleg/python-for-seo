

class Predator:

    def eating(self):
        print('I want meet!!!')
        super().eating()


class Wolf(Predator):
    wool_length = 'medium'

    def wooo(self):
        print('Woooooooooo!')

    def __add__(self, other):
        flock = (self, other)
        print('We are flock of the wolfs!', flock)
        return flock

    def eating(self):
        print('I am Wolf! And i want to eat ships!!!')
        super().eating()


class Kenguru:

    def jamp(self):
        self.__bag()
        print('AAAAAAAAAAAAAA!')

    def __bag(self):
        print('I has bag!', self)

    def eating(self):
        print('I am Kenguru! And i want to eat green trees!!!')


class Dog(Wolf, Kenguru):
    # name = 'Tuzik'
    # weight = 5.5
    # height = 0.8

    wool_length = 'short'

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def gav(self):
        print('GAV! GAV! GAV!')

    @property
    def say_name(self):
        self.gav()
        print('My name is: ', self.name)
        self.gav()
        return ''

    def wooo(self):
        self.gav()

    @staticmethod
    def eating():
        print('I am dog! And i want to eat meet!!!')

    def __lt__(self, other):
        return (self.weight*self.height) < (other.weight*other.height)

    def __le__(self, other):
        return (self.weight*self.height) <= (other.weight*other.height)

    def __eq__(self, other):
        return (self.weight*self.height) == (other.weight*other.height)

    def __ne__(self, other):
        return (self.weight*self.height) != (other.weight*other.height)

    def __ge__(self, other):
        return (self.weight*self.height) >= (other.weight*other.height)

    def __str__(self):
        return f'<DOG: {self.name} | {self.weight} kg>'

    def __repr__(self):
        return f'<DOG: {self.name} | {self.weight} kg>'

    def __del__(self):
        print('Тузик уничтожен!')


if __name__ == '__main__':
    tuzik = Dog('Tuzik', 0.8123, 0.2234)

    gavrik = Dog('Gavrik', 0.63498, 0.3)

    del tuzik



