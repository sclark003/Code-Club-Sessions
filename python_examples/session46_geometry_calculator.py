# geometry_calculator.py
# A program with functions for geometry calculations

import math

def rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def circle_area(radius):
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

def triangle_area(base, height):
    """Calculate the area of a triangle"""
    return 0.5 * base * height

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

# Main program
print("Geometry and Utility Calculator")
print("=" * 40)

# Rectangle
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
area_rect = rectangle_area(length, width)
print(f"Rectangle area: {area_rect:.2f}")

# Circle
radius = float(input("\nEnter circle radius: "))
area_circle = circle_area(radius)
print(f"Circle area: {area_circle:.2f}")

# Triangle
base = float(input("\nEnter triangle base: "))
height = float(input("Enter triangle height: "))
area_triangle = triangle_area(base, height)
print(f"Triangle area: {area_triangle:.2f}")

# Temperature conversion
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit:.2f}°F")

# Even/odd check
number = int(input("\nEnter a number: "))
if is_even(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print("\n" + "=" * 40)
print("Calculations complete!")
