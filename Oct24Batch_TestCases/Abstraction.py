from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,numberOftires):
        self.numberOftires = numberOftires
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stops")

class Car(Vehicle):
    def __init__(self):
        super().__init__(2)
    def start(self):
        print("Car starts")

class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)
    '''def start(self):
       print("Bike start")'''

'''b = Bike()
b.start()
b.stop()'''

v = Vehicle(3)
v.stop()