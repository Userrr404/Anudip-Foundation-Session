# 1. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 
# def read_file(file_path):
#     try:
#         file = open(file_path,"r")
#         content = file.read()
#         print(content)
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' does not exist.")

# # FILE IS EXIST
# read_file("C:/Users/yoges/student.txt")

# # FILEIS NOT EXIST
# read_file("C:/Users/yoges/demo.txt")


# 2. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
def raise_error(prompt):
    user_input = input(prompt)
    if not user_input.isdigit():
        raise TypeError(f"Input '{user_input}' is not a valid number")
    # return int(user_input)

try:
    num1 = raise_error("Enter num 1: ")

    num2 = raise_error("Enter num 2: ")
    print(f"The numbers you entered are {num1} and {num2}.")
except TypeError as e:
    print(e)

