# 1. Imagine you are developing a personal finance tracking application. 
#   Create a custom module named finance.py that includes functions for calculating expenses, income, and savings. 
#   Describe the functions you would include and how you would import this module in your main application.

import finance

# Example data
expenses = [200, 150, 50, 500]  # List of expenses
incomes = [2500, 1500]  # List of income sources
savings_goal = 5000  # Savings target

# Examples
total_expenses = finance.calculate_total_expenses(expenses)
total_income = finance.calculate_total_income(incomes)
savings = finance.calculate_savings(total_income, total_expenses)
progress = finance.savings_goal_progress(savings, savings_goal)

# Display results
print(f"Total Expenses: Rs{total_expenses:.2f}")
print(f"Total Income: Rs{total_income:.2f}")
print(f"Savings: Rs{savings:.2f}")
print(f"Savings Goal Progress: {progress:.2f}%")

# 2: 
#   ● Import the random module as rnd and generate a random integer between 1 and 100. 
#   ● Import the math module and calculate the square root of 49 and the sine of 90 degrees (convert degrees to radians using math.radians).in python

import random as rnd  # Import random module as rnd
import math  # Import math module

# Generate a random integer between 1 and 100
random_number = rnd.randint(1, 100)
print(f"Random Number (1-100): {random_number}")

# Calculate the square root of 49
sqrt_49 = math.sqrt(49)
print(f"Square Root of 49: {sqrt_49}")

# Calculate the sine of 90 degrees
sine_90 = math.sin(math.radians(90))  # Convert degrees to radians first
print(f"Sine of 90 degrees: {sine_90}")
