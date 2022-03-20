""" Python Notes - Classes """



" Create Class " 

#Creates a new data type (beside string, numeric, boolean)

class Student:  # Student - name of class
    def __init__(self, name, major, gpa):  # initialize function and define "student"
        self.name = name  # each student has a name
        self.major = major  # each student has a major
        self.gpa = gpa  # each student has a gpa

# Objects within the class

student1 = Student('Jim', 'Business', 4.0)  # student1 is an object - an actual student
print(student1.name)  # can call specific qualities of this student
