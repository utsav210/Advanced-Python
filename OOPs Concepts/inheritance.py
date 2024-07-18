'''
Challenge/Task:

1. Define a class ElectricCar that inherits from the Car class.
2. Add an attribute battery_size to the ElectricCar class.
3. Override the display_info method to include battery size.
'''
# Define the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Define the ElectricCar class inheriting from Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Call the parent class's constructor using super()
        super().__init__(make, model, year)
        self.battery_size = battery_size
    
    # Override the display_info method to include battery size
    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size} kWh")

# making
electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
electric_car.display_info()