def choice(func):
    def pri():
        print("adding two nos")
        func()
        print("sucess")
    return pri
@choice
def sum():
    print(4+5)

sum()