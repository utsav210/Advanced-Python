'''
Challane/Task:

1. Create a lambda function to add two numbers and assign it to a variable add.
2. Use the lambda function to add two numbers and print the result.
'''
# lambda function can have any number of arguments but only one expression.
add = lambda x, y : x + y # lambda function takes x and y as an arguments 

# print(add(5, 3.6)) # 8.6
result = add(5, 3.6)
print(result)

