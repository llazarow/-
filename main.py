class Person:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name)

person = Person("Lazar")
person.speak()

class Rectangle:
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height
    def area(self):
        area = self.wight * self.height
        print(area)

Rectangle =Rectangle(10,20)
Rectangle.area()
