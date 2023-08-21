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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        #Actions to execute: putting all items into a list
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    @property
    #Property Dcorator = read only attribute
    def name(self):
        return self.__name


    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is more than 10 characters!")

        else:
            self.__name = value



    def calculate_total_price(self):
        return self.__price * self.quantity

    
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
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}','{self.quantity}')"


    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello user.
        We have{self.name}{self.quantity} times.
        Regards, Dev_Eddy
        """

    def __send(self):
        pass


    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()