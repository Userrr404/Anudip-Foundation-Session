# Restaurant Management System :  

# Scenario: You are helping a restaurant manage its menu. The restaurant has a regular menu and a special weekend menu. 

# Tasks: 
# 1. Create a set regular_menu with items 'pizza', 'burger', 'salad', and 'pasta'. 
# 2. Create another set weekend_menu with items 'steak', 'salmon', 'pasta', and 'wine'. 
# 3. Find out which items are available on both the regular and weekend menus.
# 4. Determine the items that are only available on the weekend. 
# 5. Add a new item 'dessert' to both menus. 
# 6. The restaurant decides to stop offering 'burger'. Remove it from the regular menu.

regular_menu = {"pizza","burger","salad","pasta"}
weekend_menu = {"steak","salmon","pasta","wine"}

# Find out which items are available on both the regular and weekend menus.
available_on_both = regular_menu.intersection(weekend_menu)
print("Following items are available on both menus: ",available_on_both)

# only available on the weekend
only_weekend_items = weekend_menu.difference(regular_menu)
print("Items only available on the weekend: ",only_weekend_items)

# Add a new item 'dessert' to both menus.
regular_menu.add("dessert")
weekend_menu.add("dessert")

# The restaurant decides to stop offering 'burger'. Remove it from the regular menu.
regular_menu.discard("burger")

print("Updated Regular menu: ",regular_menu)
print("Updated Weekend menu: ",weekend_menu)


# Event Management System 

# Scenario: You are organizing a large event and need to manage the list of attendees. Some attendees have VIP access, while others do not. 

# Tasks: 
# 1. Create a set of attendees with names 'John', 'Jane', 'Emily', and 'Michael'. 
# 2. Create a frozenset vip_attendees with names 'Jane' and 'Michael'. 
# 3. A new attendee 'Sarah' registers for the event. Add her to the attendees set. 
# 4. Check if 'Emily' is a VIP attendee.
# 5. Find out which attendees have either regular or VIP access but not both. 
# 6. List all attendees with either regular or VIP access.
    
# CHECK VIP OR NOT  
def vip_Or_Not(name,vip_attendees):
    vip = name in vip_attendees
    if vip == True:
        print(f"{name} is VIP")
    else:
        print(f"{name} Not a VIP")

attendees = {"John","Jane","Emily","Michael"}
vip_attendees = frozenset({"Jane","Michael"})

# A new attendee 'Sarah' registers for the event. Add her to the attendees set. 
attendees.add("Sarah")

# Check if 'Emily' is a VIP attendee.
vip_Or_Not("Jane",vip_attendees)

# Find out which attendees have either regular or VIP access but not both.
not_In_Both = attendees.symmetric_difference(vip_attendees)
print("Attendees with either regular or VIP access but not both: ",not_In_Both)

# List all attendees with either regular or VIP access.
all_attendees = attendees.union(vip_attendees)
print("List all attendees with either regular or VIP access: ",all_attendees)

