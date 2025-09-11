# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

student={'Rajesh':23,
         'Tanu':90,
         'Yana':89,
         'Visu':56}

user_input=input("Enter the students's name:")
if user_input in student:
    print("{}'s marks:".format(user_input),student[user_input])
else:
    print("Student not found.")