class Specifier:
    leaves = 2
    _leave = 5
    __lea = 10
    def __init__(self,name,salary,arole):
        self.name = name
        self.salary = salary
        self.arole = arole

sr = Specifier("Sri", 1200, "ASE")
print((sr.leaves))
print((sr._leave))
print((sr._Specifier__lea))
