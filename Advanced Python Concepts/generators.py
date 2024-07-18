'''
1. Write a generator function countdown that takes a number and counts down to zero.
2. Iterate over the generator and print each number.
'''
import time

# define the generator function countdown
def countdown(n):
    while n >= 0:  
        yield n # pause the function and return the value of n to the caller
        n -= 1
        time.sleep(1) # wait 1 second before yielding the next value

if __name__ == "__main__":
    # iterate the each number over the generator
    for i in countdown(10):
        print(i)
