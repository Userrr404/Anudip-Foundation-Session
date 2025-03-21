# 1: Employee Salary Management (Abstraction) You are tasked with building an employee salary management system.
#  Use abstraction to create a base class Employee and two subclasses, FullTimeEmployee and PartTimeEmployee.
#   ● Abstract Class: Employee with abstract methods calculate_salary() and get_employee_details(). 
#   ● FullTimeEmployee: Overrides calculate_salary() by considering a monthly fixed salary. 
#   ● PartTimeEmployee: Overrides calculate_salary() by considering an hourly rate and hours worked.

# Task: 
#   1. Create the abstract class and its subclasses. 
#   2. Implement the salary calculation for both types of employees.
#   3. Instantiate both employee types, calculate salaries, and display their details.
#   4. Add an abstract method raise_salary() that forces both subclasses to implement their logic for raising the salary. 


from abc import ABC,abstractmethod

# BASE CLASS
class Employee(ABC):
    def __init__(self,name):
        self.name = name

    # Overrides
    @abstractmethod
    def calculate_salary(self):
        pass
        
    @abstractmethod
    def get_employee_details(self):
        pass

    @abstractmethod
    def raise_salary(self,salary):
        pass



# SUBCLASS 1
class FullTimeEmployee(Employee):
    def __init__(self,name,monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    # Overrides
    def calculate_salary(self):
        return self.monthly_salary
    
    def get_employee_details(self):
        return f"Full-Time Employee: {self.name}, Monthly Salary: Rs.{self.monthly_salary}"
    
    def raise_salary(self, salary):
        self.monthly_salary += salary
        print(f"New salary for {self.name}: Rs.{self.monthly_salary}")
    

# SUBCLASS 2
class PartTimeEmployee(Employee):
    def __init__(self, name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Overrides
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def get_employee_details(self):
        return f"Part-Time Employee: {self.name}, Hourly Rate: Rs.{self.hourly_rate}, Hours Worked: {self.hours_worked}, Salary: Rs.{self.calculate_salary()}"
    
    def raise_salary(self, salary):
        self.hourly_rate += salary
        print(f"New hourly rate for {self.name}: Rs.{self.hourly_rate}")

# CREATING OBJECTS
ft_employee = FullTimeEmployee("Alice",50000)
pt_employee = PartTimeEmployee("Bob",200, 100)

# DISPLAY DETAILS AND CALCULATE SAlARY
print(ft_employee.get_employee_details())
print(f"Salary: Rs.{ft_employee.calculate_salary()}\n")

print(pt_employee.get_employee_details())
print(f"Salary: Rs.{pt_employee.calculate_salary()}\n")

# RAISE SALARY
ft_employee.raise_salary(5000)
pt_employee.raise_salary(50)


# 2: Smart Home Devices (Encapsulation and Property Decorators) Develop a system to manage smart home devices.
#    Implement a class SmartDevice that: 
#       ● Uses encapsulation to store the device’s status (__is_on, default to False).
#       ● Has a turn_on() and turn_off() method to change the device status.
#       ● Uses a property decorator to expose the device’s status as a property (is_on) with a setter to prevent turning it on if certain conditions (like low battery) are met. 

# Task: 
#       1. Implement the SmartDevice class. 
#       2. Simulate turning the device on and off while managing conditions like low battery.
#       3. Use the property method to ensure users cannot turn on the device when the battery is below a threshold.

class SmartDevice:
    def __init__(self,battery_level = 100):
        self._is_on = False    # ENCAPSULATION
        self._battery_level = battery_level # PRIVATE VARIABLE 

    # Property to get the device status.
    @property
    def is_on(self):
        return self._is_on

    """
    Uses a property decorator to expose the device status as a property (is_on) with a setter to prevent turning it on if certain conditions (like low battery) are met.

    """
    @is_on.setter
    def is_on(self,value):
        # setter to prevent turning it on if certain conditions (like low battery)
        if value and self._battery_level < 10:
            print("Cannot turn on flash Battery is too low")
        else:
            self._is_on = value
    """
    turn_on() and turn_off() method to change the device status
    """
    def turn_on(self):
        self.is_on = True
        if self._is_on:
            print("Device is now on")
   
    def turn_off(self):
        self._is_on = False
        print("Device is now off")

    # Property to get the battery level
    @property
    def battery_level(self):
        return self._battery_level  # Return private variable
    
    @battery_level.setter
    def battery_level(self,value):
        if 0 <= value <= 100:
            self._battery_level = value
        else:
            print("Battery level must be 0 to 100") 


device = SmartDevice(battery_level=9)  # Battery is low

device.turn_on()  # Should not turn on due to low battery
device.battery_level = 50  # Charging the battery
device.turn_on()  # Should turn on now
device.turn_off()  # Should turn off successfully


