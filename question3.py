class Animal:
    def eat(self):
        pass
    def sleep(self):
        pass
class Dog(Animal):
    def bark(self):
        pass

# Create an instance of Dog
Dog1 = Dog()

#Inherited methods from Animal
Dog1.eat()
print("The Dog is eating")
Dog1.sleep()
print("the Dog is sleeping")
# Using the method specific to Dog
Dog1.bark()
print("the Dog is barking")