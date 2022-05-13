from Item import Item

item1 = Item("Phone", 350, 3)
item2 = Item("Laptop", 1000, 6)
item3 = Item("Monitor", 220, 2)
item4 = Item("HDMI", 23, 10)
item5 = Item("Mouse", 18, 8)

# Print all the items we have in our shop
print(Item.all)
# Print the price of item1 before discount
print(item1.price)
# Apply the discount
item1.discount()
# Print the price of item1 after discount
print(item1.price)
