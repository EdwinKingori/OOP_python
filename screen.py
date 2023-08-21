#applying polymophism principles in this file
from item import Item

class Screen(Item):
    pay_rate = 0.6
    def __init__(self, name: str, price: float, quantity):
        #using the super method to access methods and attributes of the prent Item class
        super().__init__(
            name, price, quantity
            )