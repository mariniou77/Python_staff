import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Check the parameters of my instances  
        assert price > 0 , f"Price of {price} is not greater than zero"
        assert quantity > 0 , f"Quantity of {quantity} is not greater than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Put all the items in one list for managing them easily
        Item.all.append(self)

    def calculate_price(self):
        return self.price * self.quantity   

    def discount(self):
        self.price = self.price * self.pay_rate   

    # With this class method I am reading the products from a csv file and immidiatle I am making instances of them  
    @classmethod
    def instantiate_from_csv(cls):
        # reading the products
        with open('OOP_with_python/products.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = list(reader)
        # Making the instances
        for item in products:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
            )            

    # With this magic function we have a prettier and more understanding view of all the instances we put in the list "all"
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"     