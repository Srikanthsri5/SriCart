class A:
    km = 1
    def met(self):
        print("this is method from class A")


class B(A):
    # km = 2
    def met(self):
        print("this is method from class B")


class C(A):
    # km = 3
    def met(self):
        print("this is method from class C")


class D(B, C):
    # km = 4
    def met(self):
        print("this is method from class D")


a = A()
b = B()
c = C()
d = D()

print(a.km)

