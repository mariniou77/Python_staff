# handle errors so the programm does not crush
from inspect import getargs


try:
    number = int(input("Enter a number : "))
    print(number)
# by setting just the exception it will cath all kind of exceptions
except:
    print("Invalid Input")   


# more specific error handling with specific excepts for individual errors
try:
    value = 10/0
    number = int(input("Enter a number : "))
    print(number) 
except ZeroDivisionError:
    print("Division by zero")        
except ValueError:
    print("Invalid Input")  

# taking the error message into a value
try:
    number = int(input("Enter a number : "))
    print(number)
# by setting just the exception it will cath all kind of exceptions
except ValueError as err:
    print(err)     