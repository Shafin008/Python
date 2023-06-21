#!/usr/bin/env python
# coding: utf-8
from item_class import Item


#item1 = Item("MyItem", 750)

# Examples for encapsulation start
# print(item1.name)

# ## Now we used a a setter decorator, we can change the value of it
# item1.name = "OtherItem"
# print(item1.name)

# # As we raised an exeption to our setter we can't use a name that has length>10
# item1.name = "OtherItemmm"
# print(item1.name)

## Though we put a restriction on price attribute--
## we can change the value by using apply_discount and apply_increment method with instance
# item1.apply_increament(0.2)
# print(item1.price)

# item1.apply_discount()
# print(item1.price)
# Examples for encapsulation ends

## Abstraction Example starts
## we can use send_email() method
#item1.send_email()

## but we can't use these methods below as these were set to private in Item class
#item1.__connect()
#item1.__prepare_body_mail()
#item1.__send()
## Abstraction Example ends

## Inheritance example starts
## first we import the class Phone which was inherited from Item class 
from Inherited_Item_Phone import Phone

# item1 = Phone("iphone", 1000, 3)
# print(item1.price)
## we can use class Item's methods here
# item1.apply_increament(0.2)
# print(item1.price)
## Inheritance example ends

##Polymorphism starts
from Inherited_Item_Keyboard import Keyboard
item1 = Item("MyItem", 100)
print(item1.price)
item1.apply_discount()
print(item1.price) ## ans should give 80

## now we'll change the default class attribute pay_rate inside Keyboard and Phone class
## pay_rate = 0.7 for Keyboard class and 0.5 for Phone class
## Note: by this change our default class attribute pay_rate will remain the same in the Item class
## It's value only change in the Keyboard and Phone class 
item2 = Keyboard("a4tech", 100, 10)
print(item2.price)
item2.apply_discount()
print(item2.price) ## ans should give 70

item3 = item1 = Phone("iphone", 100, 3)
print(item3.price)
item3.apply_discount()
print(item3.price) ## ans should give 50

## polymorphism ends








