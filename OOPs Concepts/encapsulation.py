# Description: Encapsulation is the concept of restricting access to certain methods and attributes. This is done by making attributes and methods private using a leading underscore (_) or double underscore (__).
'''
Challenge/Task:

Modify the Car class to make the make, model, and year attributes private.
Add getter and setter methods to access and modify these private attributes.
'''

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = mileage  # Private attribute

    def get_mileage(self):  # Getter method
        return self.__mileage

    def set_mileage(self, mileage):  # Setter method
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Mileage cannot be negative.")

    def drive(self, distance):
        print(f"Driving {distance} km...")
        self.__mileage += distance

# Creating a car object
my_car = Car("Toyota", "Corolla", 2022, 10000)

# Accessing attributes using getter and setter methods
print("Current mileage:", my_car.get_mileage())
my_car.drive(50)
print("Updated mileage:", my_car.get_mileage())

try: 
    # Trying to access private attribute directly (will raise an error)
    print(my_car.__mileage)

except Exception as e:
    print(f"Error: {e}")  