# Task: Convert integers to floats, floats to integers, strings to integers, and vice versa.
# Type casting
# 1. Implicit Type Casting
x = 10  # Integer
y = 2.5 # Float

z = x + y

print(z, type(z))

# 2. Explicit Type Casting
# conversion in integers
x = int(1) # 1 
print(x, type(x)) # type() returns the type of data type
y = int(5.6) # 5
print(y, type(y))
z = int("7") # 7
print(z, type(z))

# conversion in float 
a = float(5) # 5.0
print(a, type(a))
b = float(7.6) # 7.6 
print(b, type(b))
c = float("4") # 4.0
print(c, type(c))

# conversion in strings
p = str(10) # '10'
print(p, type(p))
q = str(5.6) # '5.6' 
print(q, type(q))
r = str("s1") # 's1'
print(r, type(r))