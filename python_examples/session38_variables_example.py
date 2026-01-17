# variables_example.py
# Demonstrating different data types

# String variables
name = "Sarah"
favourite_colour = "blue"
school = "Code Club School"

# Integer variables
age = 12
grade = 7
favourite_number = 42

# Float variables
height = 1.65
weight = 45.5
temperature = 23.5

# Boolean variables
is_student = True
likes_coding = True
is_weekend = False

# Display information using f-strings
print("=" * 40)
print("Student Information")
print("=" * 40)
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Grade: {grade}")
print(f"Height: {height} metres")
print(f"Favourite colour: {favourite_colour}")
print(f"Favourite number: {favourite_number}")
print(f"\nIs a student: {is_student}")
print(f"Likes coding: {likes_coding}")
print(f"Is weekend: {is_weekend}")

# Check data types
print("\n" + "=" * 40)
print("Data Types")
print("=" * 40)
print(f"name is: {type(name)}")
print(f"age is: {type(age)}")
print(f"height is: {type(height)}")
print(f"is_student is: {type(is_student)}")
