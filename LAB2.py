#1. Using input function take two number and then swap the number
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")

print("Before swap num 1: ", num1)
print("Before swap num 2: ", num2)

temp = num1
num1 = num2
num2 = temp

print("After swap num 1: ", num1)
print("After swap num 2: ", num2)

#2. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
rupees = 200
years = 5
ratePer = 5

interset = (rupees * ratePer * years) /100
print("The simple interset: ", interset)


