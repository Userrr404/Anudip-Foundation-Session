# 1. WAP to create a tuple and append another tuple to it
#    get the count of total members & repeated members
#    similarly print length of this new tuple

tuple1 = (1,2,3,4,5)
print("Tuple 1: ",tuple1)

tuple2 = (4,5,6,7,8)
print("Tuple 2: ",tuple2)

# Append the new tuple to the initial tuple
append_tuple = tuple1 + tuple2
print("Append tuple: ",append_tuple)

# Get the count of total members
total_mem = len(append_tuple)
print("Total members are: ",total_mem)

# Get the count of repeated members
repeate_mem = total_mem - len(set(append_tuple))
print("Reapeted members count: ",repeate_mem)

# Get length of append_tuple
print("Total members are: ",total_mem)



#2. WAP to to deduce use of sorting in tuples.
initial_tuple = (5,3,1,2,4)
print("Initail tuple: ",initial_tuple)

# Convert the tuple to a list
list_temp = list(initial_tuple)

# sort the list
list_temp.sort()

sorted_tup = tuple(list_temp)

print("Soreted tuple: ",sorted_tup)

