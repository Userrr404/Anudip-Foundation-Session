#1. Write a Python script to read a CSV file with missing values and replace the
#missing values with a default value (e.g., "Unknown" or 0).
#Sample Data (missing_data.csv):

#Name, Age, City
#Alice, , New York
#Bob, 25,
#Charlie, 35, Chicago

import csv

# OPEN THE FILE
with open('missingData.csv','r') as file:
    # READ THE FILE
    csv_reader = csv.reader(file)

    header = next(csv_reader)

    cleaned_data = [header]

    for row in csv_reader:
        name = row[0] if row[0] else "Unknown"
        age = str(row[1]) if str(row[1]) else "0"
        city = row[2] if row[2] else "Unknown"

        cleaned_data.append([name,age,city])

with open('modify_data.csv','w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(cleaned_data)

print("Missing values replaces and data stored to 'modify_data.csv'")

# Open the CSV file in read mode ('r')
with open('modify_data.csv', mode='r') as file: 
     # Create a CSV reader object to iterate through the file
    csv_reader = csv.reader(file)

    # Read the first row (header) to skip it
    header = next(csv_reader) 
    for row in csv_reader:
        print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")


# 2. Write a Python script to validate JSON data by checking if it contains required
# fields and if the data types are correct (e.g., integers for IDs, strings for names).
# Sample Data (data.json):

# [
#   {
#       "Product ID": 101,
#       "Name": "Widget A",
#       "Price": 25.50
#   },
#   {
#       "Product ID": "102",
#       "Name": "Widget B",
#       "Price": "40.00"
#   }
# ]

import json

# Load JSON Data from File
with open('data.json', 'r') as file:
    data = json.load(file)

# Define Expected Data Types
required_fields = {
    "Product ID": int,
    "Name": str,
    "Price": float
}

# Function to Validate JSON Data
def validate_data(data):
    for index, item in enumerate(data):
        print(f"Validating Product {index + 1}...")

        # Check if all required fields are present
        for field, dtype in required_fields.items():
            if field not in item:
                print(f"Error: '{field}' is missing in Product {index + 1}")
                continue

            # Check if the data type is correct
            if not isinstance(item[field], dtype):
                print(f"Error: '{field}' has invalid data type in Product {index + 1}. Expected {dtype.__name__}.")
            else:
                print(f"'{field}' is valid in Product {index + 1}")

    print("\nValidation Completed.")

# Call the Function
validate_data(data)