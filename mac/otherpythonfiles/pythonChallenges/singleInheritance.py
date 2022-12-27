class Employee:
    no_leaves = 8
    def __init__(self,name,salary,arole):
        self.name = name
        self.salary = salary
        self.arole = arole

class Staff(Employee):
    def disp(self,expe):
        self.expe = expe
        return f'Name is {self.name} working as {self.arole} from {self.expe}years earning INR{self.salary} per month his remaing leaves is {self.no_leaves}'


sri = Staff("Srikanth", 14000, "ASE")
print(sri.disp(2))