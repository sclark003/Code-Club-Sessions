# utility_functions.py
import math

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return math.pi * radius ** 2

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Test the functions
print(f"Rectangle area (5x3): {rectangle_area(5, 3)}")
print(f"Circle area (radius 4): {circle_area(4):.2f}")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")
