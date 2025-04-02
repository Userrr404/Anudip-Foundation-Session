# 1: Create a program that greets the user based on the current time 
#    (e.g., "Good Morning" before noon, "Good Afternoon" in the afternoon, and "Good Evening" in the evening). 
#    Use the datetime module to retrieve the current time and conditionally display a greeting. Output:
from datetime import datetime

def greet_user():
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "Good Morning"
    elif current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    print(greeting)

greet_user()


# 2: Write a Python program that asks the user to input two dates (in YYYY-MM-DD format) 
#    and calculates the number of days between the two dates. Use the datetime module to perform the calculation
from datetime import datetime

def calculate_days_between():
    date_format = "%Y-%m-%d"

    # Get user input for two dates
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")

    try:
        # Convert string input to datetime objects
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)

        # Calculate the difference in days
        difference = abs((date2 - date1).days)

        print(f"The number of days between {date1_str} and {date2_str} is {difference} days.")
    except ValueError:
        print("Invalid date format! Please enter dates in YYYY-MM-DD format.")

calculate_days_between()
