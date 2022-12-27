class Pyth:
    eleg="effpy"
    def __init__(self,name):
        self.name = name

    def displa(self):
        return self.name

class WebDev:
    # eleg="effWD"
    def __init__(self,name,ntopics):
        self.name = name
        self.ntopics = ntopics

    def displa(self):
        return self.name, self.ntopics

class PyWebdev(WebDev,Pyth):
    pass
    # eleg = "effBoth"

sri = PyWebdev("Srikanth","nodeReact")

print(sri.eleg)