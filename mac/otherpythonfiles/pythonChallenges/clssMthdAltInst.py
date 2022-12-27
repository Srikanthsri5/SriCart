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
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

adv = "Lorem-ipsum-dolor"
ssr = Employee.from_str(adv)
# sri.updateLeaves(12)
# print(sri.no_leaves)

print(ssr.printdetails())