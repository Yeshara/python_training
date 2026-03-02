"""
PYTHON 
Choose your level:
🟢 Easy | 🟡 Medium | 🔴 Hard
"""

print("\n=== SECTION 1: VARIABLES & MANAGING DATA ===")

# 🟢 EASY:
# Store your name and age and print them.

# 🟡 MEDIUM:
# Store name, age, and city.
# Print: "My name is ___, I live in ___, and I am ___ years old."

# 🔴 HARD:
# Ask the user for their name and age using input()
# Print a formatted introduction.



print("\n=== SECTION 2: DATA TYPES & STRING MANIPULATION ===")

price = 49.99
quantity = 3

# 🟢 EASY:
# Print the total cost.

# 🟡 MEDIUM:
# Print: "Total cost: R___"

# 🔴 HARD:
# Round to 2 decimal places and format as currency.



print("\n=== SECTION 3: CONTROL FLOW ===")

temperature = 18

# 🟢 EASY:
# If temperature > 25 print "Hot" else print "Cold"

# 🟡 MEDIUM:
# Add "Comfortable" for 15–24

# 🔴 HARD:
# Ask the user for temperature input and classify it.



print("\n=== SECTION 4: LOGICAL OPERATORS ===")

age = 19
has_ticket = True
is_member = False

# 🟢 EASY:
# Allow entry if age >= 18

# 🟡 MEDIUM:
# Allow entry if age >= 18 AND has_ticket

# 🔴 HARD:
# Allow entry if age >= 18 AND (has_ticket OR is_member)



print("\n=== SECTION 5: LISTS ===")

expenses = [120, 75, 90, 45]

# 🟢 EASY:
# Print the list.

# 🟡 MEDIUM:
# Add a new expense and print total.

# 🔴 HARD:
# Print total, highest expense, and average.



print("\n=== SECTION 6: LOOPS ===")

numbers = [3, 7, 10, 2, 8]

# 🟢 EASY:
# Print each number.

# 🟡 MEDIUM:
# Print each number and whether it is Even or Odd.

# 🔴 HARD:
# Count how many even numbers exist.



print("\n=== SECTION 7: DICTIONARIES ===")

employee = {
    "name": "Thabo",
    "department": "Finance",
    "salary": 25000
}

# 🟢 EASY:
# Print the employee name.

# 🟡 MEDIUM:
# Increase salary by 10% and print it.

# 🔴 HARD:
# Add a new key "bonus" and compute total pay.



print("\n=== SECTION 8: NESTING ===")

company = {
    "employee": {
        "name": "Sara",
        "skills": ["Python", "SQL", "Excel"]
    }
}

# 🟢 EASY:
# Print the employee name.

# 🟡 MEDIUM:
# Print the first skill.

# 🔴 HARD:
# Print all skills using a loop.



print("\n=== SECTION 9: FUNCTIONS ===")

# 🟢 EASY:
# Create a function that prints "Welcome!"

# 🟡 MEDIUM:
# Create a function that greets a person by name.

# 🔴 HARD:
# Create a function that greets a person and tells them the length of their name.



print("\n=== SECTION 10: FUNCTIONS WITH OUTPUT ===")

# 🟢 EASY:
# Create a function that adds two numbers.

# 🟡 MEDIUM:
# Return the result instead of printing it.

# 🔴 HARD:
# Create a function that calculates final price including 15% VAT.



print("\n=== SECTION 11: DEBUGGING ===")

total = 0
prices = [10, 20, 30]

for price in prices:
    total = total + price

print("Total is " + total)  # fix this

# 🔴 HARD:
# Modify code so it handles an empty list safely.