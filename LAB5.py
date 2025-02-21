# 1. Write a python program to reverse a number using a while loop.
# num = 123
# reverse = 0
# while num != 0:
#     # Get the last digit of the number
#     rem = num % 10
#      # Add the digit to the reverse number
#     reverse = (reverse * 10) + rem
#     # Remove last element of num & type cast
#     num =int(num / 10)

# print(reverse)

# 2. Write a python program to check whether a number is palindrome or not?
num = 1001
temp = num
reversed = 0
while num != 0:
    # Get the last digit of the number
    rem = num % 10
    # Add the digit to the reverse number
    reversed = (reversed * 10) + rem
    # Remove last element of num & type cast
    num =int(num / 10)

if reversed == temp:
    print("Palindrome")
else:
    print("Not a Palindrome")
