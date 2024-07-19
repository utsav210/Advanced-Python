'''
Task: Create a decorator log_methods that logs the entry and exit of every method call within a class.
'''
# The functools module is for higher-order functions: functions that act on or return other functions
import functools

# decorator to log method calls of a class
def log_methods(cls):
    # iterate over the attributes of the class
    for attr_name, attr_value in cls.__dict__.items():
        # check if the attribute is callable (i.e., a method)
        if callable(attr_value):
            # Replace the method with a wrapped version that logs calls
            setattr(cls, attr_name, log_method(attr_value))
    return cls

# make helper decorator to log entry and exit of a single method
def log_method(method):
    # Preserve the original method's metadata
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        # Get the class name and method name
        class_name = args[0].__class__.__name__
        method_name = method.__name__
        # Log the entry with method name and arguments
        print(f"Entering {class_name}.{method_name} with args={args[1:]} kwargs={kwargs}")
        # Call the original method
        result = method(*args, **kwargs)
        # Log the exit with method name and result
        print(f"Exiting {class_name}.{method_name} with result={result}")
        return result
    return wrapper

# log_methods decorator
@log_methods
class MathCalculations:
    def __init__(self):
        print("Hello, Sir!!!")
        return None
    # addition method that squares the input
    def square(self, x):
        return x ** 2

    # addition method that adds two inputs
    def add(self, y, z):
        return y + z

# Create an instance of MathCalculations
m1 = MathCalculations()

# Call method1 and method2 to see logging in action
m1.square(5)
m1.add(3, 4)


