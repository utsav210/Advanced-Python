'''
Objective: Create a simple employee management system that allows adding new employees, calculating average salary, and displaying employee details.

Class Method - Add Employee: Use a class method to add new employees to a class-level list. Each employee should have a unique ID, name, and salary.
Static Method - Average Salary: Implement a static method to calculate the average salary of all employees. This method should work without needing to instantiate the class.
Instance Method - Display Details: Define an instance method to display an employee’s details. It should print the employee’s ID, name, and salary.
'''
# uuid provide a way to generate unique identifiers that are practically guaranteed to be unique across space and time.
# import uuid

class Employee:
    employees = []  # Class-level list to store all employees
    next_id = 1  # Class-level attribute to track the next unique ID

    def __init__(self, name, salary):
        """Assign straight forward unique_id"""
        self.id = Employee.next_id  
        Employee.next_id += 1
        """Generate unique ID using UUID"""
        # self.id = uuid.uuid1()
        self.name = name
        self.salary = salary

    @classmethod
    def add_employee(cls, name, salary):
        new_employee = cls(name, salary)
        cls.employees.append(new_employee)
        return new_employee

    @staticmethod
    def average_salary():
        if not Employee.employees:
            return 0  # Avoid division by zero if there are no employees
        total_salary = sum(employee.salary for employee in Employee.employees)
        return total_salary / len(Employee.employees)

    def display_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}")

def main():
    # Adding employees
    emp1 = Employee.add_employee("Mahesh", 50000)
    emp2 = Employee.add_employee("Ram", 60000)
    emp3 = Employee.add_employee("Krishna", 55000)

    # Calculating average salary
    average_salary = Employee.average_salary()
    print(f"Average Salary: {average_salary}")

    # Displaying employee details
    emp1.display_details()
    emp2.display_details()
    emp3.display_details()

if __name__ == "__main__":
    main()