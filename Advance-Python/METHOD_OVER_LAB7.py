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
print(product1.display_info())  # Basic info
print(product2.display_info())
print(product1.display_info(detailed=True))  # Detailed info
print(product2.display_info(detailed=True))  # Detailed info

# Static and class methods
print(Product.product_info())
print(Customer.customer_info())
print(Order.order_info())

print("Total Products: ",Product.get_total_products())  # Total products
print("Total customers: ",Customer.get_customer_count())  # Total customers
print("Total orders: ",Order.get_order_count())  # Total orders

    