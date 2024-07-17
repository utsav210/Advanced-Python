# Task: Assign values to variables, perform operations with variables, and demonstrate variable reassignment.

# Assign values to variable 
a = 5
print(a, type(a))
b = 6.9
print(b, type(b))

# Many values to variables
w, x, y, z = "Orange", "Banana", "Cherry", "Watermelon"
print(w)
print(x)
print(y)
print(z)

# one value to multiple variables
m = n = o = "Orange"
print(m)
print(n)
print(o)

# unpack a collection and assign it to the variables
cars = ["Lamborghini", "Ferari", "Mercedes"]
p,q,r = cars 
print(p)
print(q)
print(r)

# Global Variable
x = "interpreted"

def demo():
    # local variable
    y = 85 
    print("Python is " + x + "language")
    print(y)
demo()


# operations with variables
x = 5 # int
y = 10.5 # float
result = x + y
print("Addition:", result, type(result)) # result will be float


carname = "volvo"
modelname = "XC60" 
print(carname + " " + modelname) # string concatenation

# Variable Reassignment
x = 100  # Assigning the initial value of 10 to variable x
print(x)

x = 20  # Reassigning the value of x to 20
print(x)