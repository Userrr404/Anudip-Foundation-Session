# 1. Accept a name from the user and display that in lower case using lower() function
name = input("Enter the name: ")
print("Your name in lowercase is: ",name.lower())


# 2. Write a function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. 
# Test it with different numbers
def check(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negitive"
    else:
        return "Zero"
    
num = int(input("Enter the num: "))
result = check(num)
print(f"You entered number is {num}",result)