# 1. Write a function in Python to count and display the total number of words in a text file “ABC.txt” 
# also count uppercase / lowercase character in same  text file

def count(file_path):
    upper_case = 0
    lower_case = 0
    with open(file_path,"r") as file:
        content = file.read()
        words = content.split()
        total_words = len(words)

        for char in content:
            if char.isupper():
                upper_case += 1
            else:
                if char.islower():
                    lower_case += 1
    

    print("Toatal numbers in file: ",total_words)
    print("Total uppercase character in file: ",upper_case)
    print("Total lowercase character in file: ",lower_case)

count("C:/Users/yoges/student.txt")





# 2. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words(file_path):
    try:
        with open(file_path,"r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        

display_words("C:/Users/yoges/story.txt")