import csv

class Item:
    pay_rate = 0.8 # The payrate after 20% discount
    all = []
    #method def
    def __init__(self, name: str, price: float, quantity):
        #Run validations to the received argument using  assert
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute: putting all items into a list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
# chackig if num is integer using a static method
    @staticmethod
    def is_integer(num):
        #counting the floats that are point zero (2.0,7.0,20.0)
        if isinstance(num,float):
            #counting floats that are point zero using the is_integer() method
            return num.is_integer()
        elif isinstance (num, int):
            return True
        else:
            return False
    #using the __repr__() mmethod to provide a string representation of an object
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}','{self.quantity}')"
