class Employee:
    def calculate_salary(self):
        print("Calculating salary for employee...")

class Manager(Employee):
    def calculate_salary(self):
        # Overriding the method to provide a specific calculation for a manager
        base_salary = 50000
        bonus = 10000
        total_salary = base_salary + bonus
        print(f"Manager's salary calculated: {total_salary}")

# Demonstrating method overriding
employee = Employee()
manager = Manager()

# Calls the method from Employee
employee.calculate_salary()
# Calls the overridden method from Manager
manager.calculate_salary()
