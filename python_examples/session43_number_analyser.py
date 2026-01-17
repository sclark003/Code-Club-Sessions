# number_analyser.py
# A program that analyses a number

print("Number Analyser")
print("=" * 30)

# Get a number from the user
number = int(input("Enter a number: "))

print(f"\nAnalysing the number: {number}")
print("-" * 30)

# Check if positive, negative, or zero
if number > 0:
    print("✓ The number is POSITIVE")
elif number < 0:
    print("✓ The number is NEGATIVE")
else:
    print("✓ The number is ZERO")

# Check if even or odd
if number % 2 == 0:
    print("✓ The number is EVEN")
else:
    print("✓ The number is ODD")

# Check if single digit or multiple digits
if abs(number) < 10:
    print("✓ The number is a SINGLE DIGIT")
else:
    digits = len(str(abs(number)))
    print(f"✓ The number has {digits} DIGITS")

# Check if divisible by 3
if number % 3 == 0:
    print("✓ The number is divisible by 3")
else:
    print("✓ The number is NOT divisible by 3")

# Check if it's a perfect square (simple check)
if number >= 0:
    import math
    root = math.sqrt(number)
    if root == int(root):
        print(f"✓ The number is a PERFECT SQUARE ({int(root)}²)")
    else:
        print("✓ The number is NOT a perfect square")

print("=" * 30)
