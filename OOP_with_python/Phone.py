from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, release_date=0):

        super().__init__(name, price, quantity)
        self.release_date = release_date
    # overate the __repr__ function of the Item class to add the release 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.release_date})"     