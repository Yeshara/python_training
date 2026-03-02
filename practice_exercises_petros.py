"""
PYTHON 
Choose your level:
🟢 Easy | 🟡 Medium | 🔴 Hard
"""

print("\n=== SECTION 1: VARIABLES & MANAGING DATA ===")

# 🟢 EASY:
# Store your name and age and print them.
name_easy = "Petros"
age_easy = 23
print(f"Hi, my name is {name_easy}, and I am {age_easy} years old.")

# 🟡 MEDIUM:
# Store name, age, and city.
# Print: "My name is ___, I live in ___, and I am ___ years old."
name_med = "Petros"
age_med = 23
city_med = "Johannesburg"
print(f"My name is {name_med}, I live in {city_med}, and I am {age_med} years old.")

# 🔴 HARD:
# Ask the user for their name and age using input()
# Print a formatted introduction.
name_hard = input("Please provide your first name: ")
age_hard = input("Please input your age: ")
print(f"Good day everyone, my name is {name_hard}, and my age is {age_hard}")

print("\n=== SECTION 2: DATA TYPES & STRING MANIPULATION ===")

price = 49.99
quantity = 3

# 🟢 EASY:
# Print the total cost.
print(f"Total Cost: {price*quantity}")

# 🟡 MEDIUM:
# Print: "Total cost: R___"
print(f"Total Cost: R{price*quantity}")
# 🔴 HARD:
# Round to 2 decimal places and format as currency.
print(f"Total Cost: R{price*quantity:,.2f}")
