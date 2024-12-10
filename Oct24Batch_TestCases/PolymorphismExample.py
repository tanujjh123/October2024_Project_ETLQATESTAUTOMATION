# Polymprphism : many form

# Ways to implement Polymorphism in Python

# way 1 - Method overloading ( This is not possible in Python as Python executes step by step
# and last method is already considered
class Math:
    def add(self, a,b):
         return a + b
    def add(self,a,b,c):
         return a+b+c

math = Math()

#print(math.add(3,2))
''' 
Can't be called as last method "def add(self,a,b,c):" prevails
TypeError: Math.add() missing 1 required positional argument: 'c'
'''
print(math.add(3,2,4))  # 9 - works

# way 2 : Method Overriding ( using a same method in parent and child class and child method
# fly() method takes diffrent form ( behaves differently based on implemetaions below )

# Case 1: Penguine class overrides fly() menthod
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguine(Bird):
    def fly(self):
        print("Bird can't fly")

b = Penguine()
b.fly() # Bird can't fly

# Case 2: Penguine class simple inherits fly() menthod
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguine(Bird):
    pass

b1 = Penguine()
b1.fly()  # Bird can fly


# Case 3: Create an object of Bird class - fly() method called from Bird class
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguine(Bird):
    def fly(self):
        print("Bird can't fly")

b1 = Bird()
b1.fly()  # Bird can fly

# way 3 : Operator overloading

class OperatorOverloading:
    def __init__(self,num1,num2,str1,str2):
        self.sum_of_numbers =  num1 + num2
        self.concatenation_of_strings = str1+str2

    def printMehthod(self):
        print(self.sum_of_numbers)
        print(self.concatenation_of_strings)

o = OperatorOverloading(10,20,"etlqa ","labs")
o.printMehthod()
