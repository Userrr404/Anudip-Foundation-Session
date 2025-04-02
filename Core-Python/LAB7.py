# 1. WAP to print count of uppercase, lowercase, numbers and special characters in a string.
# print count seperately.

def countChar(str):
    upper = 0
    lower = 0
    special = 0
    digits = 0

    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
    print("Numbers:", digits)
    print("Special characters:", special)

str = "This is a LAB 7 program 1 example of date !! 21-02-25"
countChar(str)

# 2. WAP with several string methods.
str1 = "lab 7 example 2."

# print the length of string
print(len(str1))

# print the uppercase of string
print(str1.upper())

# print the lowercase of string
print(str1.lower())

# print the replace a character of string
print(str1.replace('a', '2'))

# print the index of charcter of string
print(str1.find('e'))

# print the capitalize of string first character
print(str1.capitalize())

