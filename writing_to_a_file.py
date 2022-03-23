# 
# with "a" means append to a file
employees_file = open("employees.txt", "a")

employees_file.write("\nNikos Paras - Logistis")

employees_file.close()

# creating a new file 
employees_file_new = open("employeesNew.txt", "w")

employees_file_new.write("This is a new file")

employees_file_new.close()