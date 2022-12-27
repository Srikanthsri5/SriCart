
class Emp:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def disp(self):
        return f"my name is {self.name}, salary is {self.salary} "

Name = input("enter name")
Salary = int(input("enter the salary: "))
sri = Emp(Name, Salary)

print(sri.disp())
