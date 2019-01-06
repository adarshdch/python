"""
Purpose:    Inheritance Example
Author:     Adarsh Kumar
Keywords:   Multi-line comment, Single line comment, inheritance
"""

# import class_example
# or
from class_example import Student

#class HighSchoolStudent(class_example.Student):

class HighSchoolStudent(Student):
    school_name = "Green Field High School"

    def get_school_name(self):
        return "High School Student"
    
    # Override base class method and extend it
    def get_name_capitalized(self):
        return "HS: " + super().get_name_capitalized()

rajesh = HighSchoolStudent("rajesh")
print(rajesh.get_name_capitalized())
print(rajesh.get_school_name())
