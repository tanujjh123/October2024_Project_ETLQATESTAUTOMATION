class Bird:
    def __init__(self,name):
        self.name =  name


    def flyable(self):
        print(self.name+ " can fly: ")

    def signing(self):
        print(self.name+" can sing")

    def _dance(self):
        print(self.name+" can dance")

    def __eat(self):
        print(self.name+" can eat")

class Peacock(Bird):
    def __init__(self,name):
        self.name =  name

peacock = Peacock("peacock")
peacock.signing()
peacock.flyable()
peacock._dance()


