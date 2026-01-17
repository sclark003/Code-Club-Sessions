# number_analyser.py
# A program that analyses a list of numbers

print("Number Analyser")
print("=" * 40)

# Get numbers from user
numbers = []
print("Enter 5 numbers:")

for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

# Calculate statistics
total = 0
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    total += number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

average = total / len(numbers)

# Display results
print("\n" + "=" * 40)
print("Results")
print("=" * 40)
print(f"Numbers entered: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

# Count even and odd numbers
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"\nEven numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
