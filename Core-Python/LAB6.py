# 1. Python program to check if the given string is a palindrome 

def isPalindrome(str):
    reverse_str = str[::-1]

    if(str == reverse_str):
        print("Is Palindrome")
    else:
        print("Is Not Palindrome")

str = "abcba"
print("Original string: ",str)
result = isPalindrome(str)

str1 = "Hello"
print("Original string: ",str1)
result = isPalindrome(str1)


# 2. Python program to check if a given number is an Armstrong number

def isArmstrong(num,count):
    sum = 0

    for i in num:
        sum = sum + int(i)**count

    if sum==int(num):
        print("Armstrong number")
    else:
        print("Not armstrong no")


num = 153
given_num = str(num)
count = 0
while num != 0:
    num = num // 10
    
    count = count + 1

result = isArmstrong(given_num,count)
