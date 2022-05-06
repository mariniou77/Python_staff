class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def pass_grade(self):
        if self.gpa >= 3 :
            return False
        else :
            return True        