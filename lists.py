#create a list
lucky_numbers = [42, 8, 23, 15, 16,  4]
friends = ["antonis", "xristos", "dimitris", "iasonas", "antonis", "paulos"]

# print all the elements
print(friends)

# access individual element of a list
print(friends[1])

# access from the back of the list just with negatives
print(friends[-1])

# access to a range in a list without the last of my choice number (3)
print(friends[1:3])

# modify an element in the list
friends[1] = "mixalis"
print(friends[1])

# functions with lists
# append an element to the end of a list
friends.append("tomas")
print(friends)

# insert an element into a specific place in the list
friends.insert(1, "giorgos")
print(friends)

# remove an element from the list
friends.remove("giorgos")
print(friends)

# remove the last element of a list
friends.pop()
print(friends)

# get the index (position) of an element in the list
print(friends.index("mixalis"))

# count how many times an element exists in the list
print(friends.count("antonis"))

# sort a list (by default is ascending order)
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

# sort a list in descending order
# first you sort it in ascending order and then you call the reverse function
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

# copy a list 
friends2 = friends.copy()
print(friends2)

# append lists 
friends2.extend(lucky_numbers)
print(friends2)

# remove everything from a list
friends.clear()
print(friends)

