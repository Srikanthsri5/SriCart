class Comp():
    def __init__(self):
        pass

    def details(self, name, desig, salary):
        self.name = name
        self.desig = desig
        self.salary = salary


    def display(self):
        if self.salary <= 10000:
            return f"my name is {self.name}, designation is {self.desig}, salary is {self.salary} "
        else:
            return f"my name is {self.name}, designation is {self.desig}"

    def update(self, salary, hike):
        self.salary = salary + salary* (hike/100)






c = Comp()

c.name=input("your name: ")
c.desig = input("your designation: ")
c.salary = int(input("your salary: "))
print((c.display()))
ab = c.update(c.salary,hike=int(input(f"enter % of hike: ")))


print((c.display()))
