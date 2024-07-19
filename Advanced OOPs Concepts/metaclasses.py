'''
Task: Create a metaclass SingletonMeta that ensures only one instance of a class can be created.
'''

# Metaclass that ensures only one instance of the class exists.
class SingletonMeta(type):
    
    _instances = {}  # Dictionary to keep track of instances
    
    def __call__(cls, *args, **kwargs):
        # If the class does not have an instance, create one
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        # Return the existing instance
        return cls._instances[cls]

    # initialization of all attributes dct holds the class's namespace during its creation
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._custom_init()  # Call a custom class method after creation

    def __new__(mcs, name, bases, dct):
        # Modify class attributes during class creation
        dct['singleton_class_attr'] = 'This is a singleton class attribute'
        return super().__new__(mcs, name, bases, dct)

    def __prepare__(name, bases):
        # Prepare a namespace for the class before it is created
        return {}
    
# Class that uses SingletonMeta as its metaclass to ensure a single instance
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value  # Assign the value to the instance variable
    @classmethod
    def _custom_init(cls):
        # Custom initialization logic
        cls.custom_initialized = True
    
    def singleton_method(self):
        return "This method belongs to the singleton class"

# Create the first instance of SingletonClass
Singleton1 = SingletonClass("first instance")
# Attempt to create the second instance of SingletonClass
Singleton2 = SingletonClass("second instance")


# Since SingletonClass uses the singleton pattern, both instances refer to the same object
print(Singleton1.value)  #  first instance
print(Singleton2.value)  #  first instance

# Check if both instances refer to the same object
print(Singleton1 is Singleton2)  # True

# Check the singleton class attribute
print(Singleton1.singleton_class_attr)  # This is a singleton class attribute

# Check the custom initialization
print(SingletonClass.custom_initialized)  # True

# Check the singleton method
print(Singleton1.singleton_method())  # This method belongs to the singleton class