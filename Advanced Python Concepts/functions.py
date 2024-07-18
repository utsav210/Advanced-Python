'''
Challenge/Task:

1. Define a function greet that takes a name as an argument and prints a greeting message.
2. Define a function calculate_area that takes length and width as arguments and returns the area of a rectangle.
'''

# function to greet that takes a name as an argument and prints a greeting message
import datetime
def greet(name):
    current_time = datetime.datetime.now()
    hour = current_time.hour 
    if hour >= 6 and hour < 12:
        print(f"Hello!!! Good Morning, {name}")
    elif hour >= 12 and hour < 17:
        print(f"Hello!!! Good Afternoon, {name}") 
    elif hour >= 17 and hour < 20:
        print(f"Hello!!! Good Evening, {name}")
    else:
        print(f"Hello!!! Good Night, {name}")

def calculate_area(length, width):
    '''
    Args: 
        length: length of rectangle
        width: width of rectangle
    Returns:
        area of rectangle
    '''
    print("\n Area of the Rectagle:")
    area = length * width
    return area

if __name__ == "__main__":
    name = input("Enter Your Name: ")
    greet(name)
    length=int(input("Enter the length of Ractangle: "))
    width=int(input("Enter the width of Ractangle: "))
    area = calculate_area(length, width)
    print(area)
