from Student import Student

student1 = Student("Antonis", "Data Science", 2.5, True)
student2 = Student("Dimitris", "Engineering", 3.1, False)

print("Student n.1 : \nName : " + student1.name + "\nGPA : " + str(student1.gpa))
print("------------------------------")
print("Student n.2 : \nName : " + student2.name + "\nGPA : " + str(student2.gpa))