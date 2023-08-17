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

    

#print(Item.is_integer(7))

class Phone(Item):
    def __init__(self, name: str, price: float, quantity, broken_phone=0):
        #using the super method to access methods and attributes of the prent Item class
        super().__init__(name, price, quantity)
        #Run validations to the received argument using  assert
        #assert price >= 0, f"price {price} is not greater than or equal to zero!"
        #assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"
        assert broken_phone >= 0, f"broken_phone {broken_phone} is not greater or equal to zero"
        
        # Assign to self object
        #self.name = name
        #self.price = price
        #self.quantity = quantity
        self.broken_phone = broken_phone
        
        

phone1 = Phone("samsung", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("apple", 700, 5, 2)
print(phone2.calculate_total_price())

print(Item.all)
print(Phone.all)





#Item.instantiate_from_csv()
#print(Item.all)

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