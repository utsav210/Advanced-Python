'''
Challenge/Task:

1. Define a class Car with attributes make, model, and year.
2. Create an instance of the Car class.
3. Add a method display_info that prints out the details of the car.
'''

# create the class Car(camel case convention followed) 
class Car:
    # all classes have "__init__" function that will be executed when the instance of the class is being initiated(constructor)
    # initialize the attributes like make, model, year
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    '''
    # The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return f" Car Details: \nMake: {self.make} \nModel: {self.model} \nYear: {self.year}"
    '''

    # method to display details of the car
    def display_info(self):
        print(f"Car Details: \nMake: {self.make} \nModel: {self.model} \nYear: {self.year}")

# create instance(object) of Car
sport_car = Car("Lamborghini", "Aventador", 2022)
# access/execute the display_info method of class
sport_car.display_info()

'''
print("Using __str__() function the string presentation of object:")
print(sport_car) # the string presentation of object is represented
'''
