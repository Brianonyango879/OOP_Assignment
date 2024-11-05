class Animal:
    def sound(self):
        return " generic animal sound"
class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def sound(self):
        return "Meow"

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def sound(self):
        return "Woof"

Cat1 = Cat(Animal)
print(f"The cat:", Cat1.sound())
Dog1 = Dog(Animal)
print(f"The dog:", Dog1.sound())



