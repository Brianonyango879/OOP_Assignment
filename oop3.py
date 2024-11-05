class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self, employees):
        self.employees = employees

    def calculate_total_payroll(self):
        # Calculate total payroll by summing the salary of each employee
        return sum(employee.salary for employee in self.employees)

#Employee instances
emp1 = Employee("Bob", 40000)
emp2 = Employee("Joseph", 1000)
emp3 = Employee("Habiba", 2000)

#list of Employee objects
employees = [emp1, emp2, emp3]
for employee in employees:
    print(f"Employee: {employee.name}, Salary: {employee.salary}")

# Create a Payroll instance with the list of Employee objects
payroll = Payroll(employees)

# Calculate and display the total payroll
total_payroll = payroll.calculate_total_payroll()
print(f"Total Payroll: {total_payroll}")














