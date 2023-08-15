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
        
        #Actions to execute: putting all ites into a list
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

    
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}','{self.quantity}')"

    



Item.instantiate_from_csv()
print(Item.all)

#item1 = Item('phone', 200, 5)
#item2 = Item('laptop', 1000, 3)

#item1.apply_discount()
#print(item1.price)

#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

#print(Item.__dict__)
#print(item2.pay_rate)

#print(item1.name)
#print(item2.name)
#print(item1.price)
#print(item2.price)
#print(item1.quantity)
#print(item2.quantity)