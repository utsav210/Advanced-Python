'''
Task: Create an abstract base class Shape with abstract methods area() and perimeter(), and implement concrete subclasses Circle and Rectangle.
'''

# import ABC for Abstract Base Class
from abc import ABC, abstractmethod
import math # for getting value of pie

# defined abstract base class shape
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# implemented concrete subclass circle
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi*(self.radius**2)
        return result
    
    def perimeter(self):
        result = 2*math.pi*self.radius
        return result
    
# implemented concrete subclass rectangle
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        result = self.length*self.width
        return result
    # override the 
    def perimeter(self):
        result = 2*(self.length+self.width)
        return result

def main():
    # created instances of circle and rectangle
    c1 = Circle(5)
    r1 = Rectangle(8,6)

    # display the radius, area and perimeter circle
    print(f"Circle with radius: {c1.radius}")
    print(f"Area of Circle: {c1.area()}")
    print(f"Perimeter of Circle: {c1.perimeter()}")

    # display the length, width, area and perimeter rectangle
    print(f"Rectangle has length: {r1.length} and width: {r1.width}")
    print(f"Area of Rectangle: {r1.area()}")
    print(f"Perimeter of Rectangle: {r1.perimeter()}")

if __name__ == "__main__":
    main()