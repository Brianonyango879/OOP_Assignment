class Calculator:
    # Static attribute to track the number of add() calls
    count = 0

    @staticmethod
    def add(a, b):
        # Increment the count each time add() is called
        Calculator.count += 1
        return a + b


# Using the static method add() and checking the count
result1 = Calculator.add(8, 7)
print(f"Result of addition: {result1}")
print(f"Add method called: {Calculator.count} times")

result2 = Calculator.add(11, 4)
print(f"Result of addition: {result2}")
print(f"Add method called: {Calculator.count} times")
