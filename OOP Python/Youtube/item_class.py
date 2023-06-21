#!/usr/bin/env python
# coding: utf-8

# ### Item Class
import csv
class Item:
    
    ## Class attributes 
    pay_rate = 0.8 
    
    ## we'll create an empty list here
    all_items = []
    
    ## so we set up our data types for name, price and quantity
    def __init__(self,name:str, price:float, quantity=0):
        
        ## assert and assertion error message for instances
        assert type(name) == str , f"type of name {name} should be a string"
        
        assert type(price) == float or type(price) == int , f"type of price {price} should be an float or integer"
        assert price >=0 , f"price {price} should be greater than or equal to zero"
        
        assert type(quantity) == int ,f"type of quantity {quantity} should be an integer"
        assert quantity >=0 ,f"quantity {quantity} should be greater than or equal to zero"
        
        # Assign the self object
        ## We'll set our name attribute as a read only attribute
        ## we used "__" for clean read only atttribute.  
        ## So when we'll use this attributewith an instance, we don't have to use "__"
        ## still it'll work it as a read only attribute 
        self.__name = name 

        ## We'll rename the price attribute for the entire class to __price to put a restriction
        self.__price = price
        self.quantity = quantity

         ## Actions to execute when we want to access all of our items
        Item.all_items.append(self)
  
    ## Encapsulation process start
    ## Property Decorator = Read-Only attribute
    ## Creating a function with read only attribute by using @property decorator
    ## We set this because if anyone tries to change the value of this by using instances, it'll get an Attribute Error

    @property
    def name(self):
        return self.__name ## we used "__" for clean read only atttribute

    ## If we have a read only property as above and if we want to change the value of it by using an instance,
    ## we can use another decorator to create a setter
    ## so, if we'll use a setter for our read_only attribute so that we can set new values for our instance
    @name.setter
    def name(self,value):
        ## We'll set some restriction in our setter
        ## We'll set the restriction by raising an exception for the length of the value
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    # Setting a restriction on price
    @property
    def price(self):
        return self.__price 
    ## Though we put a restriction on price attribute--
    ## we can change the value by using apply_discount and apply_increment method with instance
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        return self.__price

    def apply_increament(self, increament_value ):
        self.__price = self.__price + self.__price * increament_value
        return self.__price
    
    ## Restricting the ability to overwrite the values of your object within your setters is the Encapsulation.
    ## Encapsulation process ends 

    ## Abstraction example starts   
    ## Abstraction : Hiding unnecessary info from the user(instances)
    ## We can't use these methods with instances, because it'll be private info for the developer
    ## To make the methods private, we need to use "__" before the name of the methods

    ## Suppose we want to send an email to the manager about our product
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body_mail(self):
        return f"""
        Hello SomeOne,
        We have {self.quantity} {self.name}'s. 
        Regards,
        Shafin
        """    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect("")
        self.__prepare_body_mail()
        self.__send()
    ## Abstraction example ends

    def calculate_total_price(self):
        return self.__price * self.quantity
       
    @classmethod
    def instatciating_from_csv(cls):
        with open("items.csv", "r") as f:
            
            ## we'll open the csv as a dictionary
            reader = csv.DictReader(f)
            
            ## converting the reader as a list
            items = list(reader)
        ## using for loop to iterate over the list
        
        for i in items:
            Item(
                name = i.get("name"),
                price = float(i.get("price")),
                quantity = int(i.get("quantity"))
                )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    ## Using magic method __repr__ for representing the objects
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    
    





