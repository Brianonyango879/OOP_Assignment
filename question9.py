class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Creating two Vector objects
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Adding the two vectors
result = v1 + v2

# Displaying the result
print("v1 + v2 =", result)
