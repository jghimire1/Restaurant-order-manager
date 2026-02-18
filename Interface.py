# Project: Assignment set 7 - UI module
# Depends on: combo_menu.py, order.py & order_manager.py
# Description:  Module to take the user input and display the output
# Author: Janardan Ghimire
# Date: 12/11/2025

# importing necessary modules
from combo_menu import Combo_Menu as CM
from order import Order as O
from order_manager import Order_Manager as OM
import re
import sys


# module level variable for storing the user's order
an_order: OM = None

# main function to run the UI module
def main() -> None:
    print("\nOrder Manager by JD")
    #calling the function to create an instance of Order_Manager 
    create_order_manager_object() 

# function to create an instance of Order_Manager
def create_order_manager_object() -> None:
    global an_order
    an_order = OM()
    # calling the function to display the combo menu
    display_menu()

# function to display a menu of options for the user to choose from
def display_menu() -> None:
    print("\n----------------- Menu ----------------")
    print("1 - Add an Order")
    print("2 - Display All Orders")
    print("3 - Highest Order Total")
    print("4 - Average Order Total for a combo menu item")
    print("5 - Display sum of order totals for each combo menu item")
    print("6 - Save Orders")
    print("7 - Exit")

    # getting user's choice  and validating it 
    try:
        while True:
            
            selection: int = int(input("Enter your choice (1-7): "))

            if 1 <= selection <= 7: break 
    except:
        print("Input Error. Please enter a valid number between 1 and 7.")
        display_menu()
    else:
        print()
        call_function(selection)
# function to call the appropriate function based on the user's choice
def call_function(choice: int) -> None:
    if choice == 1: add_order()
    elif choice == 2: display_all_orders()
    elif choice == 3: highest_order_total()
    elif choice == 4: average_order_total()
    elif choice == 5: sum_of_order_totals()
    elif choice == 6: save_orders()
    elif choice == 7: exit_application()

# function to add an order to the Order_Manager instance
def add_order() -> None:
    while True:
        cust_name: str = input("Enter customer name (letters, spaces and hyphens only): ").title()
        if re.match(r"^[a-zA-Z\s\-]+$", cust_name): break 
            
        print("Invalid name. Please enter a valid name.")
    
    # get menu choice with validation 
    while True:
        try:
            menu_choice: int = int(input("Enter 1-5 for the combo menu choice (1-Box, 2-Caniac, 3-Fingers, 4-Sandwich, 5-Kids): "))
            if 1 <= menu_choice <= 5: break
            print("Invalid choice. Please enter a valid number between 1 and 5.")
        except ValueError:
            print("Input Error. Please enter a valid number between 1 and 5.")
    
    # get quantity with validation (1 - 25)
    while True:
        try:
            quantity: int = int(input("Enter the quantity for combo menu choice (1-25): "))
            if 1 <= quantity <= 25: break
            print("Invalid quantity. Please enter a valid number between 1 and 25.")
        except ValueError:
            print("Input Error. Please enter a valid number between 1 and 25.")
    
    # calling the function to create an order and add it to the Order_Manager instance 
    create_and_add_order(cust_name, menu_choice, quantity)

# function to create an order and add it to the Order_Manager instance
def create_and_add_order(cust_name: str, menu_choice: int, quantity: int) -> None: 
    combo_enum= CM(menu_choice)

    # calling function to create and add oder and print result 
    result = an_order. add_order(cust_name, combo_enum, quantity)
    print(result)

    # calling the function to display the menu again
    display_menu()

# function to display all orders in the Order_Manager instance
def display_all_orders() -> None:

    # calling the function to display all orders and print the result
    print(an_order.get_all_orders())

    # calling the function to display the menu again
    display_menu()

# function to display the highest order total in the Order_Manager instance
def highest_order_total() -> None:

    print(an_order.get_highest_order_total())
    display_menu()

# function to display the average order total for a combo menu item in the Order_Manager instance
def average_order_total() -> None:

    # get user input for combo menu item 1 to 5 
    while True:
        try:
            menu_choice: int = int(input("Enter 1-5 for the combo menu choice (1-Box, 2-Caniac, 3-Fingers, 4-Sandwich, 5-Kids): "))
            if 1 <= menu_choice <= 5: break
            print("Invalid choice. Please enter a valid number between 1 and 5.")
        except ValueError:
            print("Input Error. Please enter a valid number between 1 and 5.")
    
    # assign enumeratin value to combo_enum
    combo_enum= CM(menu_choice)

    # call method for average calculation and print result 
    print (an_order.get_average_order_total_for_menu_item(combo_enum))
    
    # calling the function to display the menu again
    display_menu()

# function to display the sum of order totals for each combo menu item 
def sum_of_order_totals() -> None:
    # call method for sum of order totals and print result 
    print(an_order.get_order_totals_by_menu_items())
    
    # calling the function to display the menu again
    display_menu()

# function to save orders to a file
def save_orders() -> None:

    # ask user if they wish to save the orders
    save_choice: str = input("Do you wish to save the orders to a file (Y or N)?: ").strip().lower() 

    if save_choice == 'y':        # calling the method to save orders to a file
        print(an_order.save_order_objects())
    
    # calling the function to display the menu again
    display_menu()  

# Function to exit the application
def exit_application() -> None:

    # ask user if they wish to exit 
    exit_choice: str = input("Do you wish to exit the application (Y or N)?: ").strip().lower()
    if exit_choice == 'y':
        print("Exiting the application.")
        sys.exit()
    else:
        display_menu()

# calling the main function to start the UI module
if __name__ == "__main__":
    main()