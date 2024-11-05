from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Area = πr²
        return math.pi * (self.radius ** 2)

# Subclass for Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        # Area = side²
        return self.side_length ** 2

# Creating instances of Circle and Square
# Circle with radius 7
circle = Circle(7)
# Square with side length 5
square = Square(5)

# Calling area() on each shape
print(f"Area of the circle: {circle.area()}")
print(f"Area of the square: {square.area()}")
