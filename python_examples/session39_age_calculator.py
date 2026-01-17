# Age calculator program
from datetime import datetime

print("Personal Information Program")
print("=" * 35)

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
current_year = datetime.now().year
age = current_year - birth_year

pets = int(input("How many pets do you have? "))

print("\n" + "=" * 35)
print(f"Hello, {name}!")
print(f"You were born in {birth_year}")
print(f"You are {age} years old")
print(f"You have {pets} pet(s)")

if pets > 0:
    print(f"That's great! {pets} pet(s) must be fun!")
else:
    print("Maybe you'll get a pet one day!")
