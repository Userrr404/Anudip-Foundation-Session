# main.py
import finance

# Example data
expenses = [200, 150, 50, 500]  # List of expenses
incomes = [2500, 1500]  # List of income sources
savings_goal = 5000  # Savings target

# Calculations
total_expenses = finance.calculate_total_expenses(expenses)
total_income = finance.calculate_total_income(incomes)
savings = finance.calculate_savings(total_income, total_expenses)
progress = finance.savings_goal_progress(savings, savings_goal)

# Display results
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Total Income: ${total_income:.2f}")
print(f"Savings: ${savings:.2f}")
print(f"Savings Goal Progress: {progress:.2f}%")
