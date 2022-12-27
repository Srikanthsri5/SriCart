class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: {0}, age: {1}".format(self.name, self.age)


t = Employee("uday", 25)
print (t)