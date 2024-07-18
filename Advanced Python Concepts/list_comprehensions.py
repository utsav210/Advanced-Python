'''
Challenge/Task:

1. Create a list of squares of numbers from 1 to 10 using a list comprehension.
2. Use a list comprehension to filter out even numbers from a list of numbers from 1 to 20.

Note: Syntax: newList = [ expression(element) for element in oldList if condition ] 
    --> expression: Represents the operation you want to execute on every item within the iterable.
    --> element: The term “variable” refers to each value taken from the iterable.
    --> iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
    --> condition: (Optional) A filter helps decide whether or not an element should be added to the new list.
'''

# 1. Create a list of squares of numbers from 1 to 10 using a list comprehension
squares = [x ** 2 for x in range(1, 11)]

# Printing the squares list
print("Squares of numbers from 1 to 10:")
print(f"list of squares of numbers from 1 to 10: {squares}")
for x in squares:
    print(x)

# 2. Use a list comprehension to filter out even numbers from a list of numbers from 1 to 20
numbers = range(1, 21)
odd_numbers = [x for x in numbers if x % 2 != 0]

# list of odd numbers
print(f"list of Odd numbers from 1 to 20: {odd_numbers}")
for x in odd_numbers:
    print(x)
