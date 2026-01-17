# grade_manager.py
# A program to manage student grades using files

import json

GRADES_FILE = "grades.json"

def load_grades():
    """Load grades from file"""
    try:
        with open(GRADES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_grades(grades):
    """Save grades to file"""
    with open(GRADES_FILE, 'w') as file:
        json.dump(grades, file, indent=2)

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("Grade Management System")
    print("=" * 40)
    print("1. Add/Update student grade")
    print("2. View all grades")
    print("3. View specific student")
    print("4. Calculate average grade")
    print("5. Remove student")
    print("6. Quit")
    print("=" * 40)

def calculate_average(grades):
    """Calculate average of all grades"""
    if not grades:
        return 0
    total = sum(grades.values())
    return total / len(grades)

# Main program
grades = load_grades()

while True:
    display_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                grades[name] = grade
                save_grades(grades)
                print(f"Grade saved for {name}!")
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")
    
    elif choice == "2":
        if not grades:
            print("\nNo grades recorded yet!")
        else:
            print("\n" + "=" * 40)
            print("All Grades")
            print("=" * 40)
            for name, grade in sorted(grades.items()):
                print(f"{name:20} {grade:6.1f}")
            print("=" * 40)
    
    elif choice == "3":
        name = input("Enter student name: ")
        if name in grades:
            print(f"\n{name}'s grade: {grades[name]}")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == "4":
        if not grades:
            print("No grades to calculate average!")
        else:
            average = calculate_average(grades)
            print(f"\nAverage grade: {average:.2f}")
            print(f"Total students: {len(grades)}")
    
    elif choice == "5":
        name = input("Enter student name to remove: ")
        if name in grades:
            del grades[name]
            save_grades(grades)
            print(f"Removed {name} from records!")
        else:
            print(f"Student '{name}' not found!")
    
    elif choice == "6":
        print("\nSaving data...")
        save_grades(grades)
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
