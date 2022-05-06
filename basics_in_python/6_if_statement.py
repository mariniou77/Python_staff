# simple if statement
is_male = True
if is_male:
    print("you are a male")


is_male = False
if is_male:
    # this will not be printed because our if condition is false
    print("you are a male")

# or opperator and else condition
is_male = True
is_tall = True
if is_male or is_tall:
    print("you are a male or you are tall")  
else:
    # if you change both the variables to false this will be printed
    print("you are neither male nor tall")

# and opperator and else condition
is_male = True
is_tall = True
if is_male and is_tall:
    print("you are a male and you are tall")  
else:
    # if you change one of the variables to false this will be printed
    print("you are either not male or not tall")

# else if condition and not function
# now by playing with the variables we have all the possible answers
is_male = True
is_tall = True
if is_male and is_tall:
    print("you are a male and you are tall") 
elif is_male and not(is_tall):
    print("you are a short male")    
elif not(is_male) and is_tall:
    print("you are not a male but you are tall")      
else:
    # if you change one of the variables to false this will be printed
    print("you are either not male and not tall")

# comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(45, 78, 9))                     
