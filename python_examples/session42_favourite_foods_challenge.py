# favourite_foods.py
foods = ["pizza", "ice cream", "chocolate"]

print("Favourite Foods")
print("=" * 20)

# Add food
new_food = input("Add a food: ")
foods.append(new_food)

# Remove food
print(f"\nCurrent foods: {foods}")
remove_food = input("Food to remove: ")
if remove_food in foods:
    foods.remove(remove_food)
    print(f"Removed {remove_food}")
else:
    print("Food not found!")

# Sort and display
foods.sort()
print(f"\nSorted foods: {foods}")
print(f"Total foods: {len(foods)}")
