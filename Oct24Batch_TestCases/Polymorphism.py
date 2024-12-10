'''print(10+20+30)
print("etl qa "+"labs")

list1 = [1,2,3,4]
name  = "etl qa labs"
print(" the size of the list is ",len(list1))
print(" the length of the string is ",len(name))
'''

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat and my name is {self.name}")

    def makeSount(self):
        print("Meow")


class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Cow and my name is {self.name}")

    def makeSount(self):
        print("Moo")

cat1 = Cat("Kitty",2.5)
cow1 = Cow("Fluffy",4)

for animal in(cat1,cow1):
    animal.makeSount()
    animal.info()

