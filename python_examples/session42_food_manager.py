# food_manager.py
# A program to manage a list of favourite foods

favourite_foods = ["pizza", "ice cream", "chocolate"]

print("Favourite Foods Manager")
print("=" * 30)

while True:
    print("\nMenu:")
    print("1. View foods")
    print("2. Add food")
    print("3. Remove food")
    print("4. Sort foods")
    print("5. Count foods")
    print("6. Quit")
    
    choice = input("\nChoose an option (1-6): ")
    
    if choice == "1":
        print("\nYour favourite foods:")
        if len(favourite_foods) == 0:
            print("  (No foods in list)")
        else:
            for i, food in enumerate(favourite_foods, 1):
                print(f"  {i}. {food}")
    
    elif choice == "2":
        food = input("Enter a food to add: ")
        if food.lower() in [f.lower() for f in favourite_foods]:
            print(f"{food} is already in the list!")
        else:
            favourite_foods.append(food)
            print(f"Added {food} to your list!")
    
    elif choice == "3":
        if len(favourite_foods) == 0:
            print("The list is empty!")
        else:
            print("Current foods:")
            for i, food in enumerate(favourite_foods, 1):
                print(f"  {i}. {food}")
            try:
                index = int(input("Enter number to remove: ")) - 1
                if 0 <= index < len(favourite_foods):
                    removed = favourite_foods.pop(index)
                    print(f"Removed {removed} from your list!")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")
    
    elif choice == "4":
        favourite_foods.sort()
        print("Foods sorted alphabetically!")
        print(f"Sorted list: {favourite_foods}")
    
    elif choice == "5":
        print(f"You have {len(favourite_foods)} food(s) in your list")
        if len(favourite_foods) > 0:
            print(f"Foods: {', '.join(favourite_foods)}")
    
    elif choice == "6":
        print("\nFinal list:")
        if len(favourite_foods) == 0:
            print("  (No foods)")
        else:
            for food in favourite_foods:
                print(f"  - {food}")
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
