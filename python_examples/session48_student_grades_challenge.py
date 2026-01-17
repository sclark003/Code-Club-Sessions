# student_grades.py
grades = {}

# Add grades
while True:
    name = input("Student name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    grade = float(input(f"Grade for {name}: "))
    grades[name] = grade

# Save to file
with open("grades.txt", "w") as file:
    for name, grade in grades.items():
        file.write(f"{name}: {grade}\n")

# Read and display
print("\nAll grades:")
with open("grades.txt", "r") as file:
    for line in file:
        print(line.strip())

# Calculate average
if grades:
    average = sum(grades.values()) / len(grades)
    print(f"\nAverage grade: {average:.2f}")
