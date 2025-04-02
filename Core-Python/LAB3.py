#1. WAP to find out electricity bill for a user 
#   Take month wise units of consumptions
#   User types are : Household user/business user/ industrial user
#  Rate per unit : Household: 2 rs / business: 5 rs / Industrial : 10 rs.

# RATE PER UNIT
household = 2
business = 5
industrial = 10

# # USER TYPE
typeUser = input("Enter what type of User: (Household, Business, Industrial)").lower()

# # SUM OF UNITS
sumOfUnits = 0

for units in range(1,13):
    monthlyUnits = int(input(f"Enter units of consumption of month {units}: "))
    sumOfUnits += monthlyUnits


# # CHECK WHICH TYPE OF USER
if(typeUser == "household"):
    print("your yearly bill is: ",household * sumOfUnits)
elif(typeUser == "business"):
    print("your yearly bill is: ", business * sumOfUnits)
else:
    print("your yearly bill is: ", industrial * sumOfUnits)


# 2. WAP to find out fare  for a user 
#   Take KM wise  distance travelled as input
#  Rate per KM : (0 to 10 ): 10 rs / (10-20 ): 5 rs / (above 20 ) : 4 rs.

#RATE PER KM
zero_to_ten = 10
ten_to_twenty = 5
twenty_above = 4

# #TAKE A DISTANCE TREVELED BY USER
distance = float(input("Enter the distance traveled (in KM): "))


if distance <= 10:
    rupees = distance * zero_to_ten
    print(f"The fare for {distance} KM is: {rupees} Rs")
elif distance <= 20 and distance > 10:
    # MINUS KM TO PRVIOUS KM   
    rupees = (10 * 10) + (distance - 10) * ten_to_twenty
    print(f"The fare for {distance} KM is: {rupees} Rs")
else:
    # MINUS KM TO PRVIOUS KM
    rupees =(10 * 10) + (10 * 5) + (distance - 20)  * twenty_above
    print(f"The fare for {distance} KM is: {rupees} Rs")

# if distance <= 10:
#     rupees = distance * zero_to_ten
#     print(f"The fare for {distance} KM is: {rupees} Rs")
# elif distance <= 20 and distance > 10:
#     rupees = (10 * 10) + (distance - 10) * ten_to_twenty
#     print(f"The fare for {distance} KM is: {rupees} Rs")
# else:
#     rupees = (10 * 10) + (10 * 5) + (distance - 20) * twenty_above
#     print(f"The fare for {distance} KM is: {rupees} Rs")

# def calculate_fare(distance):
#     if distance <= 10:
#         fare = distance * 10
#     elif distance <= 20:
#         fare = (10 * 10) + (distance - 10) * 5
#     else:
#         fare = (10 * 10) + (10 * 5) + (distance - 20) * 4
#     return fare

# # Take distance traveled as input
# distance = float(input("Enter the distance traveled (in KM): "))

# # Calculate fare
# fare = calculate_fare(distance)

# # Display the fare
# print(f"The fare for {distance} KM is: {fare} Rs")

