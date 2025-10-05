"""
This class represents individual products with basic attributes
"""

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity #stock = quantity

    def __str__(self):
        return (f"Product ID: {self.id}, "
                f"Name: {self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}")

    @property
    def stock(self):
        status = "In Stock" if self.quantity > 0 else "Out of Stock"
        return f"{status} ({self.quantity})"