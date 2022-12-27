class A:
    cv1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.cv1 = "Instance var in class A"
        self.special = "special"
class B(A):
    cv1 = "I am in class B"

    def  __init__(self):

        self.var1 = "I am inside class B's Constructor"
        self.cv1 = "Instance var in class B"
        super().__init__()
a = A()
b = B()
print(b.special,"\n", b.var1,"\n", b.cv1)