# number_collector.py
# Collect numbers until user enters 0

print("Number Collector")
print("=" * 30)
print("Enter numbers (enter 0 to finish)")

numbers = []
total = 0
count = 0

while True:
    try:
        number = float(input(f"Enter number {count + 1}: "))
        
        if number == 0:
            break  # Exit the loop when 0 is entered
        
        numbers.append(number)
        total += number
        count += 1
        
    except ValueError:
        print("Please enter a valid number!")

# Display results
print("\n" + "=" * 30)
print("Results")
print("=" * 30)

if count > 0:
    average = total / count
    
    print(f"Numbers entered: {numbers}")
    print(f"Total count: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    
    # Find largest and smallest
    largest = max(numbers)
    smallest = min(numbers)
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
else:
    print("No numbers were entered!")

print("=" * 30)
