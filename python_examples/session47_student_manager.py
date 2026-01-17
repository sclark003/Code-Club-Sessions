# student_manager.py
# A program to manage student information using dictionaries

# Initial student data
students = {
    "Sarah": {
        "age": 12,
        "grade": 7,
        "favourite_subject": "Maths",
        "email": "sarah@school.com"
    },
    "Alex": {
        "age": 13,
        "grade": 8,
        "favourite_subject": "Science",
        "email": "alex@school.com"
    },
    "Jordan": {
        "age": 12,
        "grade": 7,
        "favourite_subject": "English",
        "email": "jordan@school.com"
    }
}

print("Student Information Manager")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. View all students")
    print("2. Look up a student")
    print("3. Add a student")
    print("4. Update student information")
    print("5. Remove a student")
    print("6. Quit")
    
    choice = input("\nChoose an option (1-6): ")
    
    if choice == "1":
        print("\n" + "=" * 40)
        print("All Students")
        print("=" * 40)
        for name, info in students.items():
            print(f"\n{name}:")
            print(f"  Age: {info['age']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Favourite Subject: {info['favourite_subject']}")
            print(f"  Email: {info['email']}")
    
    elif choice == "2":
        name = input("\nEnter student name: ")
        if name in students:
            info = students[name]
            print(f"\n{name}:")
            print(f"  Age: {info['age']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Favourite Subject: {info['favourite_subject']}")
            print(f"  Email: {info['email']}")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            print(f"Student '{name}' already exists!")
        else:
            age = int(input("Enter age: "))
            grade = int(input("Enter grade: "))
            subject = input("Enter favourite subject: ")
            email = input("Enter email: ")
            students[name] = {
                "age": age,
                "grade": grade,
                "favourite_subject": subject,
                "email": email
            }
            print(f"Added {name} to the system!")
    
    elif choice == "4":
        name = input("Enter student name to update: ")
        if name in students:
            print("Enter new information (press Enter to keep current):")
            age = input(f"Age (current: {students[name]['age']}): ")
            if age:
                students[name]['age'] = int(age)
            
            grade = input(f"Grade (current: {students[name]['grade']}): ")
            if grade:
                students[name]['grade'] = int(grade)
            
            subject = input(f"Favourite Subject (current: {students[name]['favourite_subject']}): ")
            if subject:
                students[name]['favourite_subject'] = subject
            
            print(f"Updated {name}'s information!")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == "5":
        name = input("Enter student name to remove: ")
        if name in students:
            del students[name]
            print(f"Removed {name} from the system!")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == "6":
        print("\nFinal student list:")
        for name in students.keys():
            print(f"  - {name}")
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
