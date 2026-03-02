print("\n=== SECTION 1: VARIABLES & MANAGING DATA ===")

# 🟢 EASY:
# Store your name and age and print them.

name = "Kayla"
age = 24
print(f"Name: {name}, Age: {age}")

# 🟡 MEDIUM:
# Store name, age, and city.
# Print: "My name is ___, I live in ___, and I am ___ years old."
city = "Florence"
print(f"My name is {name}, I live in {city}, and I am {age} years old.")

# 🔴 HARD:
# Ask the user for their name and age using input()
# Print a formatted introduction.

user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: ")) 
print(f"Hello {user_name}, you are {user_age} years old.")



print("\n=== SECTION 2: DATA TYPES & STRING MANIPULATION ===")

price = 49.99
quantity = 3

# 🟢 EASY:
# Print the total cost.
total_cost = price * quantity
print(f"Total cost: {total_cost}")

# 🟡 MEDIUM:
# Print: "Total cost: R___"
print(f"Total cost: R{total_cost}")

# 🔴 HARD:
# Round to 2 decimal places and format as currency.
formatted_cost = f"R{total_cost: .2f}"
print(f"Total cost: {formatted_cost}")