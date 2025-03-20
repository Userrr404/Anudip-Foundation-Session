# 1: Scenario:
#  You are tasked with developing a hospital management system that
# handles different types of hospital staff: 


# Doctors, Nurses, and Administrative Staff. Each
# type of staff member has basic details such as name, ID, and department. Doctors have
# specializations, nurses have shifts, and administrative staff have roles. The system
# should allow you to display staff information and also calculate their monthly salaries
# based on their unique attributes.

# CLASS 1
class Staff:
    # staff member has basic details such as name, ID, and department.
    def __init__(self,name,staff_id,department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

    def staff_info(self):
        return f"Name: {self.name}, ID: {self.staff_id}, Department: {self.department}"
    
    def cal_salary(self):
        pass


# CLASS 2
class Doctors(Staff):
    # Doctors have specializations
    def __init__(self, name, staff_id, department,specializations,fee):
        super().__init__(name, staff_id, department)
        self.specializations = specializations
        self.fee = fee

    def staff_info(self):
        info = super().staff_info()
        return f"Info: {info}, Specializations: {self.specializations}"
    
    def cal_salary(self):
        return self.fee
    


# CLASS 3
class Nurses(Staff):
    # nurses have shifts
    def __init__(self, name, staff_id, department, shifts,hours_worked, hourly_rate):
        super().__init__(name, staff_id, department)
        self. shifts =  shifts
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def staff_info(self):
        info = super().staff_info()
        return f"Info: {info}, Shifts: {self.shifts}"
    
    def cal_salary(self):
        return self.hourly_rate * self.hours_worked * 30

# CLASS 4
class Administrative(Staff):
    # administrative staff have roles
    def __init__(self, name, staff_id, department,roles,salary):
        super().__init__(name, staff_id, department)
        self.roles = roles
        self.salary = salary

    def staff_info(self):
        info = super().staff_info()
        return f"Info: {info}, Roles: {self.roles}"
    
    def cal_salary(self):
        return self.salary
    
# EXAMPLE
doctor1 = Doctors("Yogesh Lilake",101,"Cardiology","Cardiologist",50000)
nurse1 = Nurses("Aarti Kumar",201,"Cardiology","Night",10,100)
admin1 = Administrative("Dinesh Kumawat",1,"HR","Manager",100000)

# Display information and calculate salaries
print(doctor1.staff_info())
print(f"Monthly Salary: ₹{doctor1.cal_salary()}")

print(nurse1.staff_info())
print(f"Monthly Salary: ₹{nurse1.cal_salary()}")

print(admin1.staff_info())
print(f"Monthly Salary: ₹{admin1.cal_salary()}")

# 2. : Vehicle Rental System
# Imagine you are developing a Vehicle Rental System where different types of vehicles (like Car, Bike, and Truck) are available for rent.
#   ● All vehicles have some common attributes like registration_number, brand, and rental_price_per_day.
#   ● Each type of vehicle has a different pricing strategy. For example, trucks have additional charges for heavy loads, and cars have insurance fees included.

# Task:
#   ● Design a class Vehicle with a method calculate_rental_cost(), which will be overridden in the subclasses Car, Bike, and Truck.
#   ● Use method overriding to customize the rental cost calculation for each vehicle type.
#   ● Use the super() method to access common attributes from the Vehicle class.

class Vehicle:
    def __init__(self,registration_number,brand,rental_price_per_day):
        self.registration_number = registration_number
        self.brand = brand
        self.rental_price_per_day = rental_price_per_day

    # Overridden
    # Same price for bile
    # per_days_peice * how_many_days
    def calculate_rental_cost(self,days):
        return self.rental_price_per_day * days
    
    def __str__(self):
        return f"Vehicle [Registration: {self.registration_number}, Brand: {self.brand}, Daily Price: {self.rental_price_per_day}]"

# SUBCLASS 1
class Car(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day,insurance_fees):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.insurance_fees = insurance_fees

    # Overridden
    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost + self.insurance_fees
    
    def __str__(self):
        return f"Car [Registration: {self.registration_number}, Brand: {self.brand}, Daily Price: {self.rental_price_per_day}, Insurance Fee: {self.insurance_fees}]"

# SUBCLASS 2
class Bike(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day):
        super().__init__(registration_number, brand, rental_price_per_day)

    # Overridden
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)
    
    def __str__(self):
        return f"Bike [Registration: {self.registration_number}, Brand: {self.brand}, Daily Price: {self.rental_price_per_day}]"


# SUBCLASS 3
class Truck(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day,rate_heavy_loads):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.rate_heavy_loads = rate_heavy_loads

    # Overridden
    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost + self.rate_heavy_loads
    
    def __str__(self):
        return f"Truck [Registration: {self.registration_number}, Brand: {self.brand}, Daily Price: {self.rental_price_per_day}, Heavy Load Charge: {self.rate_heavy_loads}]"
    

# EXAMPLE
car1 = Car("C101","BMW",3000,1000)
car2 = Car("C102","Farari",4000,1500)

bike1 = Bike("B1001","Yanaha",1000)
bike2 = Bike("B1002","Honda",500)

truck1 = Truck("T10","Volvo",5000,500)
truck2 = Truck("T11","Mahindra",4000,200)

print(car1)
print(f"Car1 rental cost for 3 days: {car1.calculate_rental_cost(3)}")
print(car2)
print(f"Car2 rental cost for 5 days: {car2.calculate_rental_cost(5)}")

print(bike1)
print(f"bike1 rental cost for 2 days: {bike1.calculate_rental_cost(2)}")
print(bike2)
print(f"bike2 rental cost for 5 days: {bike2.calculate_rental_cost(5)}")

print(truck1)
print(f"truck1 rental cost for 10 days: {truck1.calculate_rental_cost(10)}")
print(bike2)
print(f"truck2 rental cost for 15 days: {truck2.calculate_rental_cost(15)}")




