from phone import Phone
from screen import Screen

item1 = Phone('Nokia', 1000, 6)
item1.apply_discount()
item1.apply_increment(0.5)
print(item1.price)


item1 = Screen("screen", 200, 15)
item1.apply_discount()
print(item1.price)
print(item1.all)

#Setting an Attribute
#item1.apply_increment(0.2)
#Geting an Attribute
#print(item1.price)


