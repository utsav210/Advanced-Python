'''
Challange/Task:

1. Write a decorator time_decorator that measures the time taken by a function to execute.
2. Use the decorator on a function slow_function that sleeps for 2 seconds and then prints "Function complete"
'''
import time 

# decorator that takes function as an argument
def time_decorator(func):
    # wrapper function that will pass all args and kwargs 
    def wrapper(*args, **kwargs):
        start = time.time() # record starting time
        result = func(*args, **kwargs) # call the original function 
        end = time.time() # record the ending time
        print(f"Time taken by a function {func.__name__ }to execute is {end - start:.4f}") # .4f will return elapsed time is formatted 4 decimal places for precision
        return result
    return wrapper


# defined the slow_function that must pass through the time_decorator
@time_decorator
def slow_function():
    time.sleep(2) # sleep for 2 second to simulate a slow function 
    print("Function Executed")

# call the slow_function
slow_function()