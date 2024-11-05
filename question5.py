class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = length
            self.width = length  # If only one argument is given, it's a square
        else:
            self.length = length
            self.width = width  # If two arguments are given, it's a rectangle

    def calculate_area(self):
        return self.length * self.width


# Creating instances of Rectangle
square = Rectangle(6)          # One parameter, treated as a square
rectangle = Rectangle(6, 10)   # Two parameters, treated as a rectangle

# Calculating and displaying areas
print(f"Area of square: {square.calculate_area()}")
print(f"Area of rectangle: {rectangle.calculate_area()}")
