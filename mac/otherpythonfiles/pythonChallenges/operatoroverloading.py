class Employee:
    no_leaves = 8
    def __init__(self, name, salary, arole):
        self.name = name
        self.salary = salary
        self.arole = arole

    def printdetails(self):
        return f'Name of emp is "{self.name}", salary is INR"{self.salary}" and his designation is "{self.arole}"'

    @classmethod
    def updateLeaves(cls, upleaves):
        cls.no_leaves = upleaves

    def __add__(self, other):
        return self.arole + other.arole

    def __repr__(self):
        return self.printdetails()

    def __str__(self):
        return f'name: {self.name}'

emp1 = Employee("Harry", 14000, "Developer")
# emp2 = Employee("Kane", 13000, "Engineer")
# print("\n",emp1 + emp2)
print(repr(emp1))
