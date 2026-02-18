
# Project: Assignment set 7 - order module
# Depends on: combo_menu.py 
# Description:  order class to create an order for a customer from the combo menu
# Author: Janardan Ghimire
# Date: 12/11/2025

from combo_menu import Combo_Menu as CM 

#defining the order class 
class Order:

    # defining the combo prices as class variable in a dictionary 
    COMBO_PRICES: dict = { 
        CM.BOX: 12.99,
        CM.CANIAC: 17.29,
        CM.FINGERS: 10.39,
        CM.SANDWICH:11.79,
        CM.KIDS: 6.99
    }

    # defining the initializer method 
    def __init__(self, cust_name: str, menu_choice: CM, quantity: int)-> None:
        self.cust_name = cust_name
        self.menu_choice = menu_choice
        self.quantity = quantity
    
    # getter for order total 
    @property
    def order_total(self) -> float:
        return self.__calc_order_total()
    
    # defining the private method to calculate order total
    def __calc_order_total(self) -> float:

        return Order.COMBO_PRICES[self.menu_choice] * self.quantity
    
    # defining the string method to return the string representation of the order
    def __str__(self) -> str:
        return f"Customer Name: {self.cust_name}, Menu choice: {self.menu_choice.name} Combo, Quantity: {self.quantity}, Order Total: ${self.order_total:,.2f}"
    


    
    