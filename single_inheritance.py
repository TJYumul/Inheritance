import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Dish:
    def __init__(self, dishName, cuisine, price):
        self.dishName = dishName
        self.cuisine = cuisine
        self.price = price

    def display_dish(self):
        return f"Dish: {self.dishName}\nCuisine: {self.cuisine}\nPrice: ₱{self.price}"


class Order(Dish):
    def __init__(self, dishName, cuisine, price, payment_method, custName):
        super().__init__(dishName, cuisine, price)
        self.payment_method = payment_method
        self.custName = custName

    def order_summary(self):
        return (f"{self.display_dish()}\n"
                f"Customer Name: {self.custName}\n"
                f"Payment Method: {self.payment_method}")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order System")
        self.font = ("Arial", 14)

        # Dish Details Frame
        self.dish_frame = tk.LabelFrame(root, text="Dish Details", padx=20, pady=20, font=self.font)
        self.dish_frame.grid(row=0, column=0, padx=20, pady=20)

        # Order Details Frame
        self.order_frame = tk.LabelFrame(root, text="Order Details", padx=20, pady=20, font=self.font)
        self.order_frame.grid(row=0, column=1, padx=20, pady=20)

        # Dish Name
        tk.Label(self.dish_frame, text="Dish Name:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        self.dish_name_entry = tk.Entry(self.dish_frame, font=self.font)
        self.dish_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Cuisine
        tk.Label(self.dish_frame, text="Cuisine:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        self.cuisine_entry = tk.Entry(self.dish_frame, font=self.font)
        self.cuisine_entry.grid(row=1, column=1, padx=10, pady=10)

        # Price
        tk.Label(self.dish_frame, text="Price:", font=self.font).grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self.dish_frame, font=self.font)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        # Customer Name
        tk.Label(self.order_frame, text="Customer Name:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        self.cust_name_entry = tk.Entry(self.order_frame, font=self.font)
        self.cust_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Payment Method
        tk.Label(self.order_frame, text="Payment Method:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        self.payment_method_combobox = ttk.Combobox(self.order_frame, values=["Online Payment", "Credit Card", "Cash"],
                                                    state="readonly", font=self.font)
        self.payment_method_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.payment_method_combobox.set("Online Payment")

        # Place Order Button
        self.order_button = tk.Button(self.order_frame, text="Place Order", font=self.font, command=self.place_order)
        self.order_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Order Display
        self.order_display = tk.Label(self.order_frame, text="", justify=tk.LEFT, font=self.font)
        self.order_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def place_order(self):
        try:
            # Get data from entries
            dish_name = self.dish_name_entry.get()
            cuisine = self.cuisine_entry.get()
            price = float(self.price_entry.get())  # Convert price to float
            cust_name = self.cust_name_entry.get()
            payment_method = self.payment_method_combobox.get()

            # Create order object
            order = Order(dish_name, cuisine, price, payment_method, cust_name)

            # Display order summary
            self.order_display.config(text=order.order_summary())

        except ValueError:
            # Error handling for invalid price input
            messagebox.showerror("Input Error", "Please enter valid numeric values for price.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
