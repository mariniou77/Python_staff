from Student import Student

student1 = Student("Antonis", "Data Science", 2.5)
student2 = Student("Dimitris", "Engineering", 3.1)

print("Student n.1 : \nName : " + student1.name + "\nGPA : " + str(student1.gpa))
if student1.pass_grade():
    print("Pass : Yes")
else :
    print("Pass : No")    
print("------------------------------")
print("Student n.2 : \nName : " + student2.name + "\nGPA : " + str(student2.gpa))
if student2.pass_grade():
    print("Pass : Yes")
else :
    print("Pass : No") 
