# Objective: Design a simple e-commerce system using Python classes to manage products, customers, and orders.
#            Implement instance variables, class variables, method overloading (simulated), static methods, and class methods. 

# 1. Class Definitions:     
#   ● Product Class: 
#       ○ Instance Variables:
#           ■ name: The name of the product. 
#           ■ price: The price of the product. 
#           ■ stock: The quantity available in stock. 
#       ○ Class Variables:
#           ■ total_products: A class variable to keep track of the total number of products. 

#   ● Customer Class:   
#       ○ Instance Variables: 
#           ■ name: The name of the customer. 
#           ■ email: The email address of the customer. 
#           ■ order_history: A list of orders made by the customer. 
#       ○ Class Variables:
#           ■ customer_count: A class variable to keep track of the number of customers. 

#   ● Order Class: 
#       ○ Instance Variables: 
#           ■ order_id: The unique ID for the order.
#           ■ customer: The customer who placed the order. 
#           ■ products: A dictionary of products and their quantities in the order. 
#       ○ Class Variables:
#           ■ order_count: A class variable to keep track of the total number of orders. 



# 2. Initialization: 
#   ● Product Class: 
#       ○ Initialize with name, price, and stock. Increment the total_products class variable when a new product is added.\
#   ● Customer Class: 
#       ○ Initialize with name, email, and an empty order_history. Increment the customer_count class variable when a new customer is created. 
#   ● Order Class: 
#       ○ Initialize with order_id, customer, and an empty dictionary of products. Increment the order_count class variable when a new order is created.

#  3. Instance Methods: 
#   ● Product Class: 
#       ○ update_stock(quantity): Update the stock quantity when a product is sold or restocked.
#   ● Customer Class: 
#       ○ place_order(order): Add an Order instance to the customer's order_history. 
#   ● Order Class: 
#       ○ add_product(product, quantity): Add a Product and its quantity to the order. 



# 4. Method Overloading (Simulated): 
#   ● Product Class: 
#       ○ Simulate method overloading with display_info() to show product details in different formats (basic or detailed). 



# 5. Static Methods: 
#   ● Product Class: 
#       ○ product_info(): A static method to return general information about products. 
#   ● Customer Class: 
#       ○ customer_info(): A static method to return general information about customers.
#   ● Order Class: 
#       ○ order_info(): A static method to return general information about orders.

#  6. Class Methods: 
#   ● Product Class: 
#       ○ get_total_products(): A class method to return the total number of products. 
#   ● Customer Class:  
#       ○ get_customer_count(): A class method to return the total number of customers. 
#   ● Order Class: 
#       ○ get_order_count(): A class method to return the total number of orders. 

# Instructions: 
#   1. Create the Classes: 
#       ○ Implement the Product, Customer, and Order classes based on the specifications above.


# CLASS 1
class Product:

    # CLASS VARIABLE
    total_products = 0 

    # CONSRUCTOR & INSTANCE VARIABLE
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

        # INCERSE WHEN PRODUCT IS ADDED
        Product.total_products += 1

    # Update the stock quantity when a product is sold or restocked
    def update_stock(self,quantity):
        self.stock += quantity

    def display_info(self, detailed=False):  # Simulated method overloading
        if detailed:
            return f"Product Name: {self.name}, Price: {self.price}, Stock: {self.stock}"
        else:
            return f"{self.name} :- Rs.{self.price}"
        

    @staticmethod
    def product_info():
        return "Products are items for sale in the E-commerce system"
    
    @classmethod
    def get_total_products(cls):
        return cls.total_products







# CLASS 2
class Customer:
    
    # CLASS VARIABLE
    customer_count = 0

    # CONSRUCTOR & INSTANCE VARIABLE
    def __init__(self,name,email):
        self.name = name
        self.email = email

        # EMPTY ORDER HISTORY LIST
        self.order_history = []

        # INCERSE WHEN CUSTOMER IS ADDED
        Customer.customer_count += 1

    # Add an Order instance to the customer's order_history. 
    def place_order(self,order):
        self.order_history.append(order)

    @staticmethod
    def customer_info():
        return "Customer are users who place orders in the E-commerce system"
    
    @classmethod
    def get_customer_count(cls):
        return cls.customer_count






        
# CLASS 3
class Order:

    # CLASS VARIABLE
    order_count = 0

    # CONSRUCTOR & INSTANCE VARIABLE
    def __init__(self,order_id,customer):
        self.order_id = order_id
        self.customer = customer

        # EMPTY PRODUCTS DICTONARY
        self.products = {}

        # INCRERSE WHEN PRODUCT IS ADDED
        Order.order_count += 1

    
    # Add a Product and its quantity to the order.
    def add_product(self,product,quantity):
        if product.stock >= quantity:
            self.products[product] = quantity
            product.update_stock(-quantity)
        else:
            raise ValueError("Not enough stock available.")
        
    @staticmethod
    def order_info():
        return "Orders represent a transaction made by a customer."
    
    @classmethod
    def get_order_count(cls):
        return cls.order_count

# 2. Test the Classes:    
#     ○ Create instances of Product, Customer, and Order. 
#     ○ Add products to the inventory, create orders, and place them for customers.
#     ○ Use the method overloading simulation to display product details in different formats. 
#     ○ Call static methods to get general information and class methods to get counts.

# Testing the classes
# Create products
product1 = Product("Laptop", 70000, 10)
product2 = Product("Phone", 30000, 20)

# Create a customer
customer1 = Customer("Yogesh", "yogesh@example.com")
customer2 = Customer("Abhi", "abhi123@example.com")

# Create an order
order1 = Order(1,customer1)
order2 = Order(2,customer2)

# Add products to the order
order1.add_product(product1,5)
order1.add_product(product2,1)
order2.add_product(product1,3)
order2.add_product(product2,2)

# Place the order
customer1.place_order(order1)
customer1.place_order(order2)
customer2.place_order(order1)
customer2.place_order(order2)

# Display product details
 # Basic info
print(product1.display_info()) 
print(product2.display_info())

# Detailed info
print(product1.display_info(detailed=True))  
print(product2.display_info(detailed=True))  

# Static and class methods
print(Product.product_info())
print(Customer.customer_info())
print(Order.order_info())

# Total products
print("Total Products: ",Product.get_total_products()) 

# Total customers
print("Total customers: ",Customer.get_customer_count())

# Total orders
print("Total orders: ",Order.get_order_count())  
    