# 1.Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Keys: ", dict_num.keys())
print("Values: ", dict_num.values())
print("Items: ", dict_num.items())

# 2. Write a Python program to deduce use of multiple dictionary functions.
dict_mem = {
    "name" : "Bob",
    "age" : 21,
    "city" : "mumbai",
}

# COPY THE ENTIRE DICT TO ANOTHER DICT
member = dict_mem.copy()
print("Copy of dict: ",member)

# UPDATE THE OR ADD NEW KEY VALUE PAIR
dict_mem.update(
    {"height": 5.8}
    )
print("Update the dict: ",dict_mem)

# RETURN THE LENGTH
print("Length of dict: ",len(dict_mem))

# MAKE A DICT TO STRING
print("Printable string: ", str(dict_mem))

# DELETE PARTIVULAR KEY PAIR
del dict_mem["city"]
print("After delete a city: ",dict_mem)

# RETURN THE KEYS
print("Keys: ", dict_mem.keys())

# RETURN THE VALUE
print("Values: ", dict_mem.values())

# REMOVE SPECIFIC ELEMETS WITH SPECIFIC KEY
dict_mem.pop("age")
print("After remove the age from dict: ",dict_mem)

# CLEAR DICT
dict_mem.clear()
print("After clear the dict: ",dict_mem)