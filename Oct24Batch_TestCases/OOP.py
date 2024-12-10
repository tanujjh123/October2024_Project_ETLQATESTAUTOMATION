class Student:
    '''def __init__(self,name,age):
        self.name = name
        self.age = age'''
    def __init__(self):
        self.name = "Rahul"


    def attendClass(self):
        print(self.name+" is attending classes")
    def solveAssigment(self):
        print(self.name+" is solving assignemnts")

st1 = Student()
st1.attendClass()