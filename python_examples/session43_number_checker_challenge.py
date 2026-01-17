# number_checker.py
number = int(input("Enter a number: "))

print(f"\nNumber: {number}")
print("-" * 20)

# Check positive/negative/zero
if number > 0:
    print("Type: Positive")
elif number < 0:
    print("Type: Negative")
else:
    print("Type: Zero")

# Check even/odd
if number % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")

# Check digits
num_str = str(abs(number))
if len(num_str) == 1:
    print("Digits: Single digit")
else:
    print(f"Digits: {len(num_str)} digits")
