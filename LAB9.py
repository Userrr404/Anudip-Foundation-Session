# 1. Write a Python program to get the largest and smallest number from a list without built-in functions.
list_1 = [11,2,3,4,15,6,7,8,9]
print(list_1)
largest_num = list_1[0]
smallest_num = list_1[0]

for i in list_1:
    if largest_num < i:
        largest_num = i

print("Largest number from a list: ",largest_num)

for i in list_1:
    if smallest_num > i:
        smallest_num = i

print("Smallest number from a list: ",smallest_num)

# 2. Write a Python program to find duplicate values from a list and display those.
list_2 = [1,2,2,3,4,4,5,5,6,6,6,5]
print("Original list: ",list_2)
dup_list_num = []

for i in list_2:
    if i not in dup_list_num:
        dup_list_num.append(i)

print("After removing duplicate element from original list: ",dup_list_num)

