# Project: Assignment set 7 - order_manager module
# Depends on: combo_menu.py, order.py
# Description:  Module to manage orders and their totals.
# Author: Janardan Ghimire
# Date: 12/11/2025

#importing modules
from combo_menu import Combo_Menu as CM
from order import Order 
import pickle
from pathlib import Path

#defining the Order_Manager class 
class Order_Manager: 

    # class variable to store and retrieve order objects 
    FILENAME: str = "ordersdata.dat"

    # initializing the object 
    def __init__(self) -> None:
        self.__load_order_objects()

    # instantiating the orders_dict dictionary as the getter property
    @property
    def orders_dict(self) -> dict[str, Order]:
        return self.__orders_dict
    
    # private method to load the order objects from the file (if it exists) or initialize an empty dictionary
    def __load_order_objects(self) -> None:
        file_path: Path = Path(Order_Manager.FILENAME)
        if file_path.is_file():
            try:
                with open(Order_Manager.FILENAME, "rb") as infile:
                    self.__orders_dict = pickle.load(infile)
            except Exception as e:
                print(e)
        else:
            self.__orders_dict = {}
    
    # method to add an order to the orders_dict dictionary
    def add_order(self, cust_name: str, combo_option: CM, qty: int) -> str:
        
        an_order: Order = Order(cust_name, combo_option, qty)

        self.orders_dict [an_order.cust_name] = an_order

        return f"\nAdded - {an_order}"
    
    # method to get all orders from the orders_dict dictionary  
    def get_all_orders(self) -> str: 
        result: str = "There are no orders to display."

        if self.orders_dict:
            result = "\n".join(str(order) for order in self.orders_dict.values())
        
        return result 

    # method to get the highest order total from the orders_dict dictionary
    def get_highest_order_total(self)-> str:
        result = "There are no orders to find the highest order total."

        if self.orders_dict:
            highest:float = max(order.order_total for order in self.orders_dict.values())
            result = f"The highest order total among all the orders is: ${highest:,.2f}"

            return result
    
    # method to get the average order total for a specific menu item from the orders_dict dictionary
    def get_average_order_total_for_menu_item(self, a_menu_item: CM) -> str:
        result: str = f"There are no {a_menu_item.name} combo orders."

        filtered_orders: list = [order.order_total for order in self.orders_dict.values() if order.menu_choice == a_menu_item]

        if filtered_orders:
            average_order_total: float = sum(filtered_orders) / len(filtered_orders)
        
            result = f"The average order total for {a_menu_item.name} combo orders is: ${average_order_total:,.2f}"
        
        return result
    
    # method to get the order totals by menu items from the orders_dict dictionary
    def get_order_totals_by_menu_items(self) -> str:

        result: str = "There are no orders to calculate order totals."

        if self.orders_dict:
            totals_by_menu_items: dict = {combo: 0 for combo in CM}

            for order in self.orders_dict.values():
                totals_by_menu_items[order.menu_choice] += order.order_total

            result = f"Sum of Order Totals: \n" + "\n".join(f"{combo.name} Combo: ${total:,.2f}" for combo, total in totals_by_menu_items.items())
        return result 
    
    #method to check if the order exists in the orders_dict dictionary and save the order to the file if it exists
    def save_order_objects(self):
        result: str = "No oders to save."

        if self.orders_dict:
            try:
                with open (Order_Manager.FILENAME, "wb" ) as outfile:
                    pickle.dump(self.__orders_dict, outfile)
                    result = "Orders saved."
            except Exception as e:
                print(e)
        return result 

    