# finance.py

def calculate_total_expenses(expenses):
    return sum(expenses)

def calculate_total_income(incomes):
    return sum(incomes)

def calculate_savings(income, expenses):
    return income - expenses

def savings_goal_progress(savings, goal):
    if goal <= 0:
        return 0  # Avoid division by zero
    return (savings / goal) * 100
