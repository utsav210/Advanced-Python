# Task: Perform arithmetic operations, string manipulations, and boolean comparisons. 
# Data Types

# integer operations
print("\nInteger Operation")
x = 10
y = 3
print(x, type(x)) 
print(y, type(y)) 

# arithmetic operations 
print(f"addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Modulus: {x} % {y} = {x % y}")
print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Exponentiation: {x} ** {y} = {x ** y}")

# float Operations
print("\nFloat Operation")
a = 10.5
b = 2.3
print(a, type(a)) 
print(b, type(b)) 

# arithetic operations
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division

# String Manipulations
print("\nString Manipulations:")
Greet1 = "Good"
Greet2 = "Morning"

print(f"Concatenation: {Greet1 + ' ' + Greet2}")  # Concatenation
print(f"Repetition: {Greet1 * 3}")  # Repetition
print(f"Length of '{Greet1}': {len(Greet1)}")  # Length
print(f"Uppercase: {Greet1.upper()}")  # Convert to Uppercase
print(f"Lowercase: {Greet2.lower()}")  # Convert to Lowercase
print(f"Substring: {Greet1[1:4]}")  # Substring
print(f"Replace: {Greet1.replace('l', 'x')}")  # Replace characters

print("\nBoolean Comparisons:")
m = 5
n = 10

print(m < 10 and n > 5) # logical AND
print(m > 10 or n < 5) # logical OR
print(not(m == n)) # Boolean Comparisons

# Comparing different data types
print(f"Is {x} > {y}? {x > y}")  # Greater than
print(f"Is {a} < {b}? {a < b}")  # Less than
print(f"Is '{Greet1}' == '{Greet2}'? {Greet1 == Greet2}")  # String equality
print(f"Is {x} equal to 10? {x == 10}")  # Integer equality

print("\nCombining Different Data Types:")
# Combining different data types
combined_result = Greet1 + " " + str(x)
print(f"Combined String and Integer: {combined_result}, {type(combined_result)}")

combined_result = Greet2 + " " + str(b)
print(f"Combined String and Float: {combined_result}, {type()}")