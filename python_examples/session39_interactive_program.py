# interactive_program.py
# An interactive program that gets user input

print("=" * 40)
print("Welcome to the Interactive Program!")
print("=" * 40)

# Get user's name
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

# Get user's age
age = int(input("How old are you? "))
print(f"You are {age} years old.")

# Get user's favourite colour
favourite_colour = input("What is your favourite colour? ")
print(f"{favourite_colour} is a great colour!")

# Get user's favourite number
favourite_number = int(input("What is your favourite number? "))
double = favourite_number * 2
print(f"Double your favourite number is {double}!")

# Create a summary
print("\n" + "=" * 40)
print("Summary")
print("=" * 40)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favourite colour: {favourite_colour}")
print(f"Favourite number: {favourite_number}")
print(f"Double of favourite number: {double}")

print("\nThank you for using the program!")
