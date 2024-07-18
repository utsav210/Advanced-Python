'''
Description: Polymorphism allows methods to do different things based on the object it is acting upon, even though they share the same name.

Challenge/Task:

Define a class Bike with a method start_engine that prints "Bike engine started".
Add a method start_engine to the Car class that prints "Car engine started".
Write a function start_vehicle that takes a vehicle object and calls its start_engine method.
'''

# define the class Bike
class Bike:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed

    # define the start_engine function that prints "Bike engine started"
    def start_engine(self):
        print("Bike engine started")

# define the class Car
class Car:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
    # define the start_engine function that prints "Car engine started"
    def start_engine(self):
        print("Car engine started")

# define a function start_vehicle that takes a vehicle object and calls its start_engine method.
def start_vehicle(vehicle):
    vehicle.start_engine()

# create the instances of the vehicles
car = Car("Lamborghini","Aventador", 2023, "6.5 L539 V12")
bike = Bike("Kawasaki", "Ninja ZX-10R", 2024, "300 kmph")

start_vehicle(bike)
start_vehicle(car)

