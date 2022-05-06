# by default input fanction takes the users input as a string
# so this will not work as we excepted and will just concat the two variables
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = num1 + num2
print(result)

# by this you convert the string to an integer
num3 = input("Enter a number: ")
num4 = input("Enter a number: ")
result1 = int(num3) + int(num4)
print(result1)

# by this you can aslo accept decimals
num5 = input("Enter a number: ")
num6 = input("Enter a number: ")
result2 = float(num5) + float(num6)
print(result2)