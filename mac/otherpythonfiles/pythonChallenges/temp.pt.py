class A:
    cva = "I am cv in A"
    def __init__(self):
        self.var1 = "I am inside A's Const"
        self.cve = "Instance variable"

class B(A):
    cv2 = "I am in class B"

a = A()
b = B()

print(b.cva)