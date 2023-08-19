from item import Item 

class Phone(Item):
    def __init__(self, name: str, price: float, quantity, broken_phone=0):
        #using the super method to access methods and attributes of the prent Item class
        super().__init__(
            name, price, quantity
            )
        #Run validations to the received argument using  assert
        assert broken_phone >= 0, f"broken_phone {broken_phone} is not greater or equal to zero"
        
        # Assign to self object
        self.broken_phone = broken_phone