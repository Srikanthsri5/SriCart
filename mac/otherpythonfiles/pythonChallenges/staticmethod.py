class Employee:
    no_leaves = 8
    def __init__(self,name,salary,arole):
        self.name = name
        self.salary = salary
        self.arole = arole

    def printdetails(self):
        return f'Name of emp is "{self.name}", salary is INR"{self.salary}" and his designation is "{self.arole}"'

    @classmethod
    def updateLeaves(cls,upleaves):
        cls.no_leaves = upleaves
    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def greet(string):   
        print("Hello "+ string)


sri = Employee("Sri",14000,"ASE")


sri.greet(sri.name)