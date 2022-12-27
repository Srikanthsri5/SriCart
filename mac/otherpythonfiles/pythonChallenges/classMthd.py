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


sri = Employee("Srikanth", 14000, "ASE")
sri.updateLeaves(12)
print(sri.no_leaves)