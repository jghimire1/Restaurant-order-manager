# Depends on: combo_menu.py, order.py & order_manager.py
# Description:  Module to take the user input and display the output
# Author: Janardan Ghimire

import tkinter as tk
from tkinter import messagebox
from combo_menu import Combo_Menu as CM  
from order_manager import Order_Manager as OM

class Program16_GUI:
    def __init__(self):

        #main window setup 
        self.mw = tk.Tk()
        self.mw.title("Program 16 - GUI Module")
        self.mw.option_add("*Font", "Garamond 12")
        self.mw.geometry("1150x900")

        # setting the default font and background color
        bg_color = "darkgreen"
        text_color = "white"
        buttton_color = "gold"
        button_text_color = "black"

        # setting the background color and text color for the main window
        self.mw.configure(bg=bg_color)
        
        # instantiateing the order manager
        self.order_manager = OM()

        # creating the frames for layout organization
        self.top_frame = tk.Frame(self.mw,pady=10, bg=bg_color)
        self.name_frame = tk.Frame(self.mw, pady = 10, bg=bg_color)
        self.menu_selection_frame = tk.Frame(self.mw, pady = 10, bg=bg_color)
        self.quantity_frame = tk.Frame(self.mw, pady = 10, bg=bg_color)
        self.action_frame = tk.Frame(self.mw, pady = 10, bg=bg_color)
        self.output_frame = tk.Frame(self.mw, pady = 10, bg=bg_color)
        # header section 
        self.header_label = tk.Label(self.top_frame, text="Order Manager by JD", font=("Garamond", 16, "bold"), bg=bg_color, fg=text_color)
        self.header_label.pack()

        # customer input section
        self.name_label = tk.Label(self.name_frame, text="Customer Name:", bg=bg_color, fg=text_color)
        self.name_entry = tk.Entry(self.name_frame, width=30) 

        #packing the customer name input section
        self.name_label.pack(side = "left", padx = 10)
        self.name_entry.pack(side = "left", padx = 10)

        # menu selection section - radio buttons for combo menu options
        self.menu_selection_label = tk.Label(self.menu_selection_frame, text="Select Combo Menu:", bg=bg_color, fg=text_color)
        self.menu_selection_label.pack(anchor="w")

        # variables for radio buttons to track selected menu option default to BOX = 1 
        self.combo_var = tk.IntVar()
        self.combo_var.set(1)
        self.radio_buttons = []

        # looping through the combo menu options and creating radio buttons
        for combo in CM:
            rb = tk.Radiobutton(self.menu_selection_frame, text=combo.name, value=combo.value, variable=self.combo_var, bg=bg_color, fg=text_color, selectcolor= "black", activebackground= bg_color)
            rb.pack(side="left", padx=5)
            self.radio_buttons.append(rb)
                
        # quantity input section
        self.quantity_label = tk.Label(self.quantity_frame, text="Quantity (1-25):", bg=bg_color, fg=text_color)
        self.quantity_entry = tk.Entry(self.quantity_frame, width=5)

        #packing the customer quantity input section        
        self.quantity_label.pack(side = "left", padx = 5)
        self.quantity_entry.pack(side = "left", padx = 5)

        # packing the frames
        self.top_frame.pack()
        self.name_frame.pack()
        self.menu_selection_frame.pack()
        self.quantity_frame.pack()
        self.action_frame.pack()
        self.output_frame.pack()

        
        # action section - buttons for adding and displaying orders
        button_style = {"bg": buttton_color, "fg": button_text_color, 'width':30}

        # row 1 buttons
        self.add_order_button = tk.Button(self.action_frame, text="1. Add Order", **button_style, command=self.add_order)
        self.display_orders_button = tk.Button(self.action_frame, text="2. Display All Orders", **button_style, command=self.display_orders)

        # row 2 buttons
        self.highest_total_button = tk.Button(self.action_frame, text="3. Highest Order Total", **button_style, command=self.highest_total)
        self.average_button = tk.Button(self.action_frame, text="4. Average for Selected Combo Item", **button_style, command=self.average_total)
        
        # row 3 buttons
        self.sum_orders_button = tk.Button(self.action_frame, text="5. Sum of All Orders", **button_style, command=self.sum_orders)
        self.save_orders_button = tk.Button(self.action_frame, text="6. Save Orders", **button_style, command=self.save_orders)

        # exit button
        self.exit_button = tk.Button(self.action_frame, text="7. Exit", **button_style, command=self.mw.destroy) 

    # packing the action buttons
        self.add_order_button.grid(row=0, column=0, padx=10, pady=5)
        self.display_orders_button.grid(row=0, column=1, padx=10, pady=5)
        self.highest_total_button.grid(row=1, column=0, padx=10, pady=5)
        self.average_button.grid(row=1, column=1, padx=10, pady=5)
        self.sum_orders_button.grid(row=2, column=0, padx=10, pady=5)
        self.save_orders_button.grid(row=2, column=1, padx=10, pady=5)
        self.exit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # output section - for displaying results
        self.output_text = tk.Text(self.output_frame, height=25, width=110, borderwidth=1, relief="solid")
        self.output_text.pack()

    # method to update output 
    def update_output (self, text: str):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", text)
    
    # method to add order
    def add_order(self):
        name = self.name_entry.get().strip().title() 
        try: 
            quantity = int(self.quantity_entry.get())
            combo_val = self.combo_var.get()
        except ValueError: 
            messagebox.showerror("Input Error", "Quantity must be an number.")
            return

        if not name.replace(" ", "").replace("-","").isalpha():
            messagebox.showerror("Input Error", "Customer Name  must contain only letters, spaces, or hyphens.")
            return

        if not (1 <= quantity <= 25):
            messagebox.showerror("Input Error", "Quantity must be between 1 and 25.")
            return 
        
        # creating the order and adding it to the order manager
        combo_enum = CM(combo_val)
        result = self.order_manager.add_order(name, combo_enum, quantity)

        # updating the output
        self.update_output(result)
        self.name_entry.delete(0, "end")
        self.quantity_entry.delete(0, "end")

    # method to display all orders
    def display_orders(self):
        result = self.order_manager.get_all_orders()
        self.update_output(result)
    
    # method to display the highest total order
    def highest_total(self):
        result = self.order_manager.get_highest_order_total()
        self.update_output(result)
    
    # method to display the average total for a selected combo menu item
    def average_total(self):
        combo_val = self.combo_var.get()
        combo_enum = CM(combo_val)
        result = self.order_manager.get_average_order_total_for_menu_item(combo_enum)
        self.update_output(result)
    
    # method to display the sum of all orders
    def sum_orders(self):
        result = self.order_manager.get_order_totals_by_menu_items()
        self.update_output(result)

    # method to save orders to a file
    def save_orders(self):
        result = self.order_manager.save_order_objects()
        messagebox.showinfo("Save Orders", result)
        self.update_output(result)
    
# calling main function to run the application
if __name__ == "__main__":
    app = Program16_GUI()
    tk.mainloop()

