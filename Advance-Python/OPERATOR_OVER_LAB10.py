# 1. Custom String Class: Implement a CustomString class that overloads the + operator for concatenation and the * operator to repeat the string. 
# Include a method to return the string in uppercase. 
class CustomString:
    def __init__(self, value):
        self.value = str(value)  # Ensure the value is a string

    def __add__(self, other):
        if isinstance(other, CustomString):
            return CustomString(self.value + other.value)
        return NotImplemented  # Ensures proper error handling for unsupported types

    def __mul__(self, times):
        if isinstance(times, int) and times >= 0:
            return CustomString(self.value * times)
        return NotImplemented  # Ensures correct behavior for invalid inputs

    def to_uppercase(self):
        return self.value.upper()

    def __str__(self):
        return self.value

# Example usage:
s1 = CustomString("Hello")
s2 = CustomString(" World")

# Overloaded + operator (Concatenation)
s3 = s1 + s2
print(s3) 

# Overloaded * operator (Repetition)
s4 = s1 * 3
print(s4) 

# Convert to uppercase
print(s3.to_uppercase())  

# 2. Currency Conversion: Create a Currency class that represents a monetary amount in a specific currency. 
#   Overload the + operator to add amounts in the same currency, and implement a method to convert between different currencies.

class Currency:
    # Exchange rates (1 INR to other currencies)
    exchange_rates = {
        "USD": 0.012,  # 1 INR = 0.012 USD
        "EUR": 0.011,  # 1 INR = 0.011 EUR
        "GBP": 0.0095, # 1 INR = 0.0095 GBP
        "JPY": 1.61    # 1 INR = 1.61 JPY
    }

    def __init__(self, amount):
        self.amount = float(amount)

    # Overload + operator to add amounts in INR.
    def __add__(self, other):
        if isinstance(other, Currency):
            return Currency(self.amount + other.amount)
        raise ValueError("Can only add amounts in INR.")

    # Convert the amount from INR to the target currency.
    def convert_to(self, target_currency):
        target_currency = target_currency.upper()

        if target_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {target_currency}")

        converted_amount = self.amount * self.exchange_rates[target_currency]
        return f"{converted_amount:.2f} {target_currency}"

    def __str__(self):
        # Return string representation of the amount in INR.
        return f"{self.amount:.2f} INR"

# Example usage:
inr1 = Currency(500)  # 500 INR
inr2 = Currency(300)  # 300 INR

# Adding INR amounts
total_inr = inr1 + inr2
print(total_inr)  # Output: 800.00 INR

# Convert INR to other currencies
print(inr1.convert_to("USD"))  # Convert 500 INR to USD
print(inr1.convert_to("EUR"))  # Convert 500 INR to EUR
print(inr1.convert_to("GBP"))  # Convert 500 INR to GBP
print(inr1.convert_to("JPY"))  # Convert 500 INR to JPY

