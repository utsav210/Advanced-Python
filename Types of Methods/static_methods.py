'''
Challenge/Task:

Define a class MathUtils with a static method add_numbers that takes two numbers and returns their sum.
Call the static method without creating an instance of the class.
'''
# defined the MathUtils class
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        """Static method to add two numbers"""
        return a + b
    
def main():
    a = int(input("Enter the input number A: "))
    b = int(input("Enter the input number B: "))
    
    """without creating instance of the class"""
    result = MathUtils.add_numbers(a,b)
    print(f"Sum of two numbers: {result}")

if __name__ =="__main__":
    main()