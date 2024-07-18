'''
*args --> Non-keyword Arguments
*args receives arguments as a tuple.
**kwargs --> keyword Arguments
**kwargs receives arguments as a dictionary.
'''

# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    # self allows to refer to this specific instance within the class's methods.
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]
        self.model = args[2]

# creating objects of car class
audi = Car(200, 'red', 'A5')
bmw = Car(250, 'black', 'GT630i')
lamborghini = Car(190, 'white', 'Aventador')

# printing the color and speed of the cars
print(audi.color) # red
print(bmw.speed) # 250
print(lamborghini.model) # Aventador

'''
Challenge/Task:

1. Define a function sum_all that takes any number of arguments and returns their sum using *args
2. Define a function print_info that takes any number of keyword arguments and prints them using **kwargs
'''

#function to sum all arguments using *args
def sum_all(*args):
    result = sum(args)
    return result

# function to print information as key value pairs using **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

result = sum_all(15, 25, 36, 56, 97, 49, 10, 2)
print(f"Sum of all arguments: {result}")

print_info(name='Thomas', age=32, country='England')

'''
Difference between *args and **kwargs
'''
def diff_args_kwargs(*args, **kwargs):
    print(args) # tuple of positional arguments
    print(kwargs) # dictioary of keyword arguments

diff_args_kwargs(4, 15, 26, 37, 48, 59, 70, fname='Harshad', lname='Mehta', work='stock_trading', income=500000)