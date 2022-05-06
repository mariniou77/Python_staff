# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# for loop
# in this example you loop as many letters as the string given
for letter in "Greece Thessaloniki":
    # print every value that variable letter takes each time
    print(letter)

# for loop in arrays    
friends = ["Antonis", "Xristos", "Dimitris"]
for friend in friends:
    # print every element of the array
    print(friend)

# another way to print every element of an array depending on the length of the array
for index in range(len(friends)):
    # print every element of the array
    print(friends[index])    

# for loop in a range of numbers
for i in range(10):
    print(i)    

# for loop in a specific range of numbers
for i in range(3, 10):
    print(i)      
