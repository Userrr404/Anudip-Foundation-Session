# 1. Write a Python program to Get Only unique items from two sets. 

# Input: set1 = {10, 20, 30, 40, 50} 

# set2 = {30, 40, 50, 60, 70} 

# Output: {70, 40, 10, 50, 20, 60, 30} 

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
unique_item = set1.union(set2)
print(unique_item)


# 2. Write a Python program to Return a set of elements present in Set A or B, but not both. 

# Input: set1 = {10, 20, 30, 40, 50} 

# set2 = {30, 40, 50, 60, 70} Output: {20, 70, 10, 60}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.symmetric_difference(set2)
print(result)