num1 = float(input("Enter first number : "))
operator = input("Enter the operator : ")
num2 = float(input("Enter second number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)     
else: 
    print("You have entered a wrong operator")           