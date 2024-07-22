'''
Objective: Model a family tree using multilevel inheritance where each generation inherits traits from the previous one.

Classes: Define a Grandparent class with basic attributes like surname and methods like family_origin(). Create a Parent class that inherits from Grandparent, adding attributes like education and methods like profession(). Finally, define a Child class that inherits from Parent, with additional attributes like hobbies and methods like current_school().

Implementation: Ensure that each class correctly uses the super() function to initialize the parent class attributes and methods.

Challenge: Add a method in the Child class that displays the entire family history by accessing attributes and methods from all ancestors.
'''
# defined Grandparent class
class Grandparent:
    # initialize the attributes like surname, origin, etc.
    def __init__(self, surname, origin):
        self.surname = surname
        self.origin = origin
    
    # method that display family origin
    def family_origin(self):
        return f"The {self.surname} family originates from {self.origin}."
    
# Parent class inherits the Grandparent class
class Parent(Grandparent):
    # add(initialize) some more attributes like education, profession, etc.
    def __init__(self, surname, origin, education, profession):
        # initialize the Grandparent part of parent using super()
        super().__init__(surname, origin)
        self.education = education
        self.profession = profession

    # method that display family profession
    def profession_info(self):
        return f"The {self.surname} family members have profession: {self.profession}."
    
# Child class inherits the Parent clss
class Child(Parent):
    # add(initialize) some more attributes like name, hobbies, cureent_school, etc
    def __init__(self, name, surname, origin, education, profession, hobbies, current_school):
        super().__init__(surname, origin, education, profession)
        self.name = name
        self.hobbies = hobbies
        self.current_school = current_school

    # method that display current school attend by child
    def current_school_info(self):
        return f"The {self.surname} family\'s child {self.name} is currently attend {self.current_school}."
    
    # method that returns the family history 
    def family_history(self):
        family_history =[
            self.family_origin(),
            f"Parent\'s Education: {self.education}",
            self.profession_info(),
            f"Hobbies of {self.name}: {self.hobbies}",
            self.current_school_info()
        ]
        return "\n".join(family_history) 
    
if __name__ == "__main__":
    # created instance of Child class
    child = Child(
        name = "Ivan",
        surname = "Gandhi",
        origin = "Bharuch",
        education = "M.Tech in IT",
        profession = "AI/ML Engineer",
        hobbies = "['Reading Geeta', 'Playing Cricket', 'Solving Puzzles']",
        current_school = "St.Joseph High School"
    )

    # displays the entire family history by accessing attributes and methods from all ancestors.
    print(child.family_history())