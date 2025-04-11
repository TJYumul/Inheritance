import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Dish:
    def __init__(self, dish_name, cuisine, price):
        self.dish_name = dish_name
        self.cuisine = cuisine
        self.dish_price = price

    def dish_details(self):
        return f"Dish: {self.dish_name}, Cuisine: {self.cuisine}, Price: ₱{self.dish_price}"

class Drinks:
    def __init__(self, drink_name, size, price):
        self.drink_name = drink_name
        self.size = size
        self.drink_price = price

    def drinks_details(self):
        return f"Drink: {self.drink_name}, Size: {self.size}, Price: ₱{self.drink_price}"

class Dessert:
    def __init__(self, dessert_name, sweetness_level, price):
        self.dessert_name = dessert_name
        self.sweetness_level = sweetness_level
        self.dessert_price = price

    def dessert_details(self):
        return f"Dessert: {self.dessert_name}, Sweetness Level: {self.sweetness_level}, Price: ₱{self.dessert_price}"

class Order(Dish, Drinks, Dessert):
    def __init__(self, customer_name, dish_name, cuisine, dish_price,
                 drink_name, size, drink_price, dessert_name,
                 sweetness_level, dessert_price, payment_method):
        Dish.__init__(self, dish_name, cuisine, dish_price)
        Drinks.__init__(self, drink_name, size, drink_price)
        Dessert.__init__(self, dessert_name, sweetness_level, dessert_price)
        self.customer_name = customer_name
        self.payment_method = payment_method

    def total(self):
        return self.dish_price + self.drink_price + self.dessert_price

    def order_summary(self):
        return (f"Customer Name: {self.customer_name}\n"
                f"{self.dish_details()}\n"
                f"{self.drinks_details()}\n"
                f"{self.dessert_details()}\n"
                f"Payment Method: {self.payment_method}\n"
                f"Total Price: ₱{self.total()}")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order System")
        self.font = ("Arial", 14)

        # Dish Frame
        self.dish_frame = tk.LabelFrame(root, text="Dish Details", padx=20, pady=20, font=self.font)
        self.dish_frame.grid(row=0, column=0, padx=20, pady=20)

        # Drinks Frame
        self.drinks_frame = tk.LabelFrame(root, text="Drinks Details", padx=20, pady=20, font=self.font)
        self.drinks_frame.grid(row=0, column=1, padx=20, pady=20)

        # Dessert Frame
        self.dessert_frame = tk.LabelFrame(root, text="Dessert Details", padx=20, pady=20, font=self.font)
        self.dessert_frame.grid(row=1, column=0, padx=20, pady=20)

        # Order Frame
        self.order_frame = tk.LabelFrame(root, text="Order Details", padx=20, pady=20, font=self.font)
        self.order_frame.grid(row=1, column=1, padx=20, pady=20)

        # Dish Name
        tk.Label(self.dish_frame, text="Dish Name:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        self.dish_name_entry = tk.Entry(self.dish_frame, font=self.font)
        self.dish_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Cuisine
        tk.Label(self.dish_frame, text="Cuisine:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        self.cuisine_entry = tk.Entry(self.dish_frame, font=self.font)
        self.cuisine_entry.grid(row=1, column=1, padx=10, pady=10)

        # Price for Dish
        tk.Label(self.dish_frame, text="Price:", font=self.font).grid(row=2, column=0, padx=10, pady=10)
        self.dish_price_entry = tk.Entry(self.dish_frame, font=self.font)
        self.dish_price_entry.grid(row=2, column=1, padx=10, pady=10)

        # Drink Name
        tk.Label(self.drinks_frame, text="Drink Name:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        self.drink_name_entry = tk.Entry(self.drinks_frame, font=self.font)
        self.drink_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Size
        tk.Label(self.drinks_frame, text="Size:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        self.size_entry = tk.Entry(self.drinks_frame, font=self.font)
        self.size_entry.grid(row=1, column=1, padx=10, pady=10)

        # Price for Drink
        tk.Label(self.drinks_frame, text="Price:", font=self.font).grid(row=2, column=0, padx=10, pady=10)
        self.drink_price_entry = tk.Entry(self.drinks_frame, font=self.font)
        self.drink_price_entry.grid(row=2, column=1, padx=10, pady=10)

        # Dessert Name
        tk.Label(self.dessert_frame, text="Dessert Name:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        self.dessert_name_entry = tk.Entry(self.dessert_frame, font=self.font)
        self.dessert_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Sweetness Level
        tk.Label(self.dessert_frame, text="Sweetness Level:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        self.sweetness_level_entry = tk.Entry(self.dessert_frame, font=self.font)
        self.sweetness_level_entry.grid(row=1, column=1, padx=10, pady=10)

        # Price for Dessert
        tk.Label(self.dessert_frame, text="Price:", font=self.font).grid(row=2, column=0, padx=10, pady=10)
        self.dessert_price_entry = tk.Entry(self.dessert_frame, font=self.font)
        self.dessert_price_entry.grid(row=2, column=1, padx=10, pady=10)

        # Customer Name
        tk.Label(self.order_frame, text="Customer Name:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        self.customer_name_entry = tk.Entry(self.order_frame, font=self.font)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Payment Method
        tk.Label(self.order_frame, text="Payment Method:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        self.payment_method_combobox = ttk.Combobox(self.order_frame,
                                                     values=["Online Payment", "Credit Card", "Cash"],
                                                     state="readonly", font=self.font)
        self.payment_method_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.payment_method_combobox.set("Online Payment")

        # Place Order Button
        self.order_button = tk.Button(self.order_frame, text="Place Order", font=self.font, command=self.place_order)
        self.order_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Order Summary Display
        self.order_display = tk.Label(self.order_frame, text="", justify=tk.LEFT, font=self.font)
        self.order_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def place_order(self):
        try:
            customer_name = self.customer_name_entry.get()
            dish_name = self.dish_name_entry.get()
            cuisine = self.cuisine_entry.get()
            dish_price = float(self.dish_price_entry.get())
            drink_name = self.drink_name_entry.get()
            size = self.size_entry.get()
            drink_price = float(self.drink_price_entry.get())
            dessert_name = self.dessert_name_entry.get()
            sweetness_level = self.sweetness_level_entry.get()
            dessert_price = float(self.dessert_price_entry.get())

            payment_method = self.payment_method_combobox.get()

            order = Order(customer_name, dish_name, cuisine, dish_price,
                          drink_name, size, drink_price, dessert_name,
                          sweetness_level, dessert_price, payment_method)

            self.order_display.config(text=order.order_summary())

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for price.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
