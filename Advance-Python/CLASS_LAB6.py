# Q.1 --> Create a class Employee that manages employee details:

#  1. Instance Attributes: ○ name: The employee's name. ○ salary: The employee's salary. ○ position: The employee's position. 

# 2. Methods: ○ promote(self, new_position): Updates the employee's position. '
# '           ○ update_salary(self, new_salary): Updates the employee's salary. 
#             ○ display_info(self): Displays the employee's name, position, and salary
class Employee:
    def __init__(self,name,salary,position):
        self.name = name
        self.salary = salary
        self.position = position

    # UPDATE POSITION TO NEW_POSITION
    def promote(self,new_position):
        self.position = new_position
        print(f"{self.name} has been promoted to {self.position}")

    # UPDATE SALARY TO NEW_SALARY
    def update_salary(self,new_salary):
        self.salary = new_salary
        print(f"{self.name} salary has been updated to {self.salary}")
    
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Position: {self.position}")
        print(f"Employee Salary: {self.salary}")


emp1 = Employee("Yogesh Lilake", 20000, "Junior App developer")

# DISPLAYING EMPLOYEE DETAILS
emp1.display_info()

# PROMOTING THE EMPLOYEE
emp1.promote("Senior App developer")

# UPDATING THE SALATY
emp1.update_salary(50000)

# DISPLAYING EMPLOYEE DETAILS
emp1.display_info()

# Q.2-->

# Create a class MovieLibrary that manages a collection of movies:

# 1. Class Attribute: ○ available_movies: A list of all movies available in the library. 

# 2. Instance Attributes: ○ member_name: The name of the library member. ○ borrowed_movies: A list of movies borrowed by the member. 

# 3. Methods: ○ borrow_movie(self, movie): Borrows a movie from the library if available. 
#             ○ return_movie(self, movie): Returns a movie to the library. 
#             ○ view_borrowed_movies(self): Prints a list of movies borrowed by the member

class MovieLibrary:
    available_movies = ["Witcher", "Mr. Robot", "Titanic", "Internship", "Live on"]

    def __init__(self,member_name):
        self.member_name = member_name
        self.borrowed_movies = []
    
    def borrow_movie(self,movie):
        # CHECK IF THE MOVIE IS AVAILABLE
        if movie in MovieLibrary.available_movies:
            # REMOVE THE BOOK FROM LIBRARY
            MovieLibrary.available_movies.remove(movie)  
            # ADD IT TO THE MEMBER BORROWED LIST
            self.borrowed_movies.append(movie)
            print(f"{self.member_name} borrowed '{movie}'")
        else:
            print(f"{movie} movie not available in library")

    def return_movie(self,movie):
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            # ADD BACK TO AVAILABLE MOVIES
            MovieLibrary.available_movies.append(movie) 
            print(f"{self.member_name} returned '{movie}'")
        else:
            print(f"{self.member_name} hasn't borrowed '{movie}'")

    def view_borrowed_movie(self):
        if self.borrowed_movies:
            print(f"{self.member_name} has borrowed: {', '.join(self.borrowed_movies)}")
        else:
            print(f"{self.member_name} has not borrowed any movies.")

member1 = MovieLibrary("Alice")

# VIEWING AVAILABLE MOVIES
print("Available Movies:", MovieLibrary.available_movies)

# BORROWING A MOVIE
member1.borrow_movie("Live on")
member1.borrow_movie("Matrix")

# VIEWING BORROWED MOVIES
member1.view_borrowed_movie()

# RETURNING A MOVIE
member1.return_movie("Live on")

# VIEWING AVAILABLE MOVIES AFTER RETURNING
print("Available Movies:", MovieLibrary.available_movies)