# Ctrl + K + C to comment out a block of code
# Ctrl + K + U to uncomment out a block of code

# simple function
from unittest import result


def say_hi():
    print("Hello everyone")

say_hi()    


# function with parameter
def say_hi_name(name):
    print("Hello " + name)

say_hi_name("Antonis")
inp_name  = input("Enter a name : ")
say_hi_name(inp_name)    

# function with more parameters
def say_hi_name_age(name, age):
    print("Hello " + name + ", your age is " + str(age))

say_hi_name_age("Antonis", 25)
inp_name  = input("Enter a name : ")
inp_age  = input("Enter your age : ")
say_hi_name_age(inp_name, inp_age)   

# return statement in functions
def cube(num):
    return num*num*num

result = cube(3)
print(result)    