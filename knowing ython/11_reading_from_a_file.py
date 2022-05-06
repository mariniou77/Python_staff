# opening a file from the same directory
# r = reading, w = writing, a = append, r+ = read and write
employees_file = open("employees.txt", "r")

# this will return a boolean that shows if the file is actually readable
print(employees_file.readable())

# read the whole file
print(employees_file.read())

# read individual lines and go to the next one, this will give me the first line and if i call it again it will give me the second one and goes on
print(employees_file.readline())
# reading the next line
print(employees_file.readline())

# taking every line and put it in a list
# to check this comment out the two commands above
print(employees_file.readlines())

# # access to one specific line-element of the list
# to check this comment out the command above
print(employees_file.readlines()[3])

# print all the employees in a for loop from the list tha readlines made
# # to check this comment out the commands above
for employee in employees_file.readlines():
    print(employee)

# always close the file 
employees_file.close()