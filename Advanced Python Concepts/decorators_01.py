'''
Decorator Example:

1. Write a decorator debug decorator that returns the all arguments and kwargs if given oterwise return no arguments given/passed.
'''

def debug_decorator(func):
    # wrapper function handles all the arguments and keyword arguments
    def wrapper(*args, **kwargs):
        # check for arguments or keyword arguments are passed or not
        if args or kwargs:
            args_value = ','.join(str(arg) for arg in args) if args else ''
            kwargs_value = ','.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else ''
            print(f"Calling the {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        # return message if no arguments passed
        else:
            print("No args or kwargs are passed/given")
        return func(*args, **kwargs)
    return wrapper

@debug_decorator
def greet(name, years_of_exp): 
    print(f"Hello, {name}!!!How are you? What did you learn in your past {years_of_exp} years of experience?")

@debug_decorator
def hello():
    print("Hello!!! Sir, Have a good day")

if __name__ == "__main__":
    greet("Thomas", years_of_exp=5)
    hello()