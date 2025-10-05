class AVLProduct:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

        @property
        def stock(self):
            return self.quantity > 0

        def __str__(self):
            status = "In Stock" if self.quantity > 0 else "Out of Stock"
            return (f"Product ID: {self.product_id}, Name: {self.product_name}, ")

