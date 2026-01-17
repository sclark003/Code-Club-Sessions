# student_info.py
students = {
    "Sarah": {"age": 12, "subject": "Maths"},
    "Alex": {"age": 13, "subject": "Science"},
    "Jordan": {"age": 12, "subject": "English"}
}

# Look up student
name = input("Enter student name: ")
if name in students:
    info = students[name]
    print(f"{name}: Age {info['age']}, Favourite: {info['subject']}")

# Update student
name = input("\nStudent to update: ")
if name in students:
    students[name]["age"] = int(input("New age: "))
    students[name]["subject"] = input("New subject: ")
    print("Updated!")

# Display all
print("\nAll students:")
for name, info in students.items():
    print(f"{name}: {info}")
