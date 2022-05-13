from Item import Item
from Phone import Phone

# item1 = Item("Phone", 350, 3)
# item2 = Item("Laptop", 1000, 6)
# item3 = Item("Monitor", 220, 2)
# item4 = Item("HDMI", 23, 10)
# item5 = Item("Mouse", 18, 8)

# # Print all the items we have in our shop
# print(Item.all)
# # Print the price of item1 before discount
# print(item1.price)
# # Apply the discount
# item1.discount()
# # Print the price of item1 after discount
# print(item1.price)

# If I want to make the instances from the csv file I have to comment out the lines that making manually instances 
# Item.instantiate_from_csv()
# print(Item.all)

# To check the inheritance with the Phone class comment out everuthing above
item = Item("Laptop", 1000, 6)
print(item)
phone = Phone("Iphone 12 pro max", 1380, 5, 2019)
print(phone)
print(phone.release_date)
print(Item.all)