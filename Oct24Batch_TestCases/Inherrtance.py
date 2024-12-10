class Human:
    noOfLegs = 2
    def speak(self):
        print("Human speaks")
    def eat(self):
        print("Human eats")

class Student(Human):
    name = "Rahul"
    print("My name is "+name)
    def speak(self):
        print("Student speaks")
    def sleep(self):
        print("studnet sleeping")

student = Student()
print(student.name)
student.eat()
student.speak()
student.sleep()
human = Human()
human.speak()


