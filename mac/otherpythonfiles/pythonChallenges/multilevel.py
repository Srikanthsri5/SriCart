class GrFather:
    cricket = 1

class Father(GrFather):
    study = 1

class Son(Father):
    pass
        # study = 4

sri = GrFather()
shi = Father()
abc = Son()

print(abc.cricket)