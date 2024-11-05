class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.make} Model: {self.model} Year: {self.year}")

# Usage
Car1 = Car("RangeRover", "Vogue", 2020)

# Call the display_info() method
Car1.display_info()
