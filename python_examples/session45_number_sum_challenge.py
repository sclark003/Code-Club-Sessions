# number_sum.py
numbers = []
total = 0

print("Enter numbers (0 to stop):")

while True:
    num = float(input("Number: "))
    if num == 0:
        break
    numbers.append(num)
    total += num

print(f"\nYou entered {len(numbers)} numbers")
print(f"Sum: {total}")
print(f"Numbers: {numbers}")
