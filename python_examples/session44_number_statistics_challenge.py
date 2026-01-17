# number_statistics.py
numbers = []

# Get 5 numbers
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate sum
total = 0
for num in numbers:
    total += num

# Find largest and smallest
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Calculate average
average = total / len(numbers)

# Display results
print(f"\nNumbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
