class Education():
    School = "University of Mysore"
    def __init__(self, name, quali):
        self.name = name
        self.quali = quali
    @classmethod
    def instt(cls):
        return Education.School
    def disp(self):
        return f'Your name is: {self.name} \n {self.name} is a {self.quali} graduate at {Education.School}'

Name = input("enter your name: ")
Degree = input("enter your qualification: ")

edu = Education(Name,Degree)

print(edu.disp())