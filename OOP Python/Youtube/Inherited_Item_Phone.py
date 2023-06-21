#!/usr/bin/env python
# coding: utf-8

### Phone Class (inherited from Item class)
from item_class import Item

### Creating an inheritance of class Item
class Phone(Item):
    ## Changing the pay_rate for polymorphism example
    pay_rate = 0.5
    
    def __init__(self,name:str, price:float, quantity=0, broken_phones = 0):
        
        ## Super function for inheritance
        super().__init__(name,price,quantity)
        
        ## assert and assertion error message for instances
        assert type(broken_phones) == int ,f"type of quantity {broken_phones} should be an integer"
        assert broken_phones >=0 ,f"quantity {broken_phones} should be greater than or equal to zero"
        
        # Assign the self object
        self.broken_phones = broken_phones





