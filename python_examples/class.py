
# Class Example

class Student:
    school_name = "Sinhgad School"    # Static member

    # Constructor
    def __init__(self, name, id = 0):
        self.name = name                # Property
        self.id = id
    
    def __str__(self):
        return "Student " + self.name
    
    # Method
    def get_name_capitalized(self):
        return self.name.capitalize()
    
    def get_school_name(self):
        return self.school_name
        
print(Student.school_name)              # prints "Sinhgad School"
