'''
Challenge:

Define a class Person with a private attribute _age.
Create a property method age with a getter and setter to access and modify the _age attribute.
Instantiate the Person class, set the age, and print it.
'''

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        """Getter for the age property"""
        if not hasattr(self, '_age'):
            raise AttributeError("Age attribute has been deleted")
        return self._age
    
    @age.setter
    def age(self, new_age): 
        """Setter for the age property"""
        if new_age >= 0:
            self._age=new_age
        else:
            raise ValueError("Age cannot be negative")
        
    @age.deleter
    def age(self):
        """Deleter for the age property"""
        if hasattr(self, '_age'):
            del self._age
        else:
            raise AttributeError("Age attribute has already been deleted")

def main():
    # instantiate the Person class
    person = Person(age=20)

    # print the initial age
    print(f"Initial age: {person.age}")

    # set a new age
    person.age = 25
    print(f"Updted age: {person.age}")

    # set age from user
    person.age = int(input("Enter Your age: "))
    print(f"Your age is: {person.age}")

    # deletes person age
    del person.age
    try:
        # Attempt to print age after deletion
        print(f"After deletion, age is: {person.age}")
    except AttributeError as e:
        print(f"Error occurred: {e}")
    
    try:
        person.age = -25
    except ValueError as e:
        print(f"Error Occured: {e}")

if __name__ == "__main__":
    main()