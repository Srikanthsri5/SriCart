class Car:

    def __init__(self):
        self.name = input("enter car name: ")
        self.model = "Q7"
        self.lap = self.Ambasidor()

    def dis(self):
        return f'Name of car is {self.name} and {self.model} is the model'


    class Ambasidor:

        def __init__(self):
            self.ambName = input("enter owner's name: ")

        def disAmb(self):
            return f' Owner of {Car.__name__} is {self.ambName}'


c = Car()
print(c.dis())
print(c.lap.disAmb())