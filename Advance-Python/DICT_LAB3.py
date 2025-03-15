# 1. You have a list of user data with their names and email addresses. Create a
# dictionary that maps each domain (from the email address) to a list of users with
# emails from that domain.

user_data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.org"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "David", "email": "david@example.net"},
]

domain_user_dict = {}

for user in user_data:
    name = user["name"]
    email = user["email"]
    domain = email.split('@')[1]
    
    if domain not in domain_user_dict:
        domain_user_dict[domain] = []
    
    domain_user_dict[domain].append(name)

print(domain_user_dict)

# 2. You have a list of customer reviews for different products. Each review
# contains a product name and a rating. Your task is to create a dictionary that
# maps each product to its average rating.

reviews = [
    {"product": "Product A", "rating": 4.5},
    {"product": "Product B", "rating": 3.8},
    {"product": "Product A", "rating": 4.0},
    {"product": "Product B", "rating": 4.2},
    {"product": "Product C", "rating": 5.0},
]

product_ratings = {}
rating_counts = {}

for review in reviews:
    product = review["product"]
    rating = review["rating"]
    
    if product not in product_ratings:
        product_ratings[product] = 0
        rating_counts[product] = 0
    
    product_ratings[product] += rating
    rating_counts[product] += 1

average_ratings = {product: product_ratings[product] / rating_counts[product] for product in product_ratings}

print(average_ratings)