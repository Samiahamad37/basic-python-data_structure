class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
    
    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"Sold {quantity} {self.name}(s). Remaining stock: {self.stock}")
        else:
            print(f"Not enough stock for {self.name}. Available: {self.stock}")
            
    def add_stock(self, quantity):
        if self.stock >= quantity:
            self.stock += quantity
            print(f"adding {quantity} {self.name}(s). available stock: {self.stock}")
        else:
            print(f"{self.name} Available: {self.stock}")
            
    def discount(self, amount,perce):
        self.price >= amount
        print(f"the {self.name} of {self.category} is discounted from ${self.price} to ${amount} at {perce}%")
        
        
    
    
   
    def availability(self):
        if self.stock > 0:
            print(f"The product {self.name} in {self.category} at ${self.price} is still available.")
        else:
            print(f"The {self.name} in {self.category} at ${self.price} is sold out.")


class Electronics(Product):
    def __init__(self, name, category, price, stock,warranty_period):
        super().__init__(name, category, price, stock)
        self.warranty_period =warranty_period
    
    def display_warrranty(self):
        
    




product1 = Product("Laptop", "Electronics", 1200, 10)
product1.availability()
product1.reduce_stock(5)
product1.add_stock(4)
product1.discount(1000,40)
product1.availability()
