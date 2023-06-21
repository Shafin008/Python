#!/usr/bin/env python
# coding: utf-8

### Phone Class (inherited from Item class)
from item_class import Item

### Creating an inheritance of class Item
class Keyboard(Item):

    pay_rate = 0.7
    
    def __init__(self,name:str, price:float, quantity=0):
        
        ## Super function for inheritance
        super().__init__(name,price,quantity)
        





