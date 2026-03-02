# from math import 

"""
PYTHON 
Choose your level:
🟢 Easy | 🟡 Medium | 🔴 Hard
"""

print("\n=== SECTION 1: VARIABLES & MANAGING DATA ===")

# 🟢 EASY:
# Store your name and age and print them.
my_name = "Sakaroa"
my_age = 23

print(f'Name: {my_name}, Age: {my_age}')


# 🟡 MEDIUM:
# Store name, age, and city.
# Print: "My name is ___, I live in ___, and I am ___ years old."
my_city = "Windhoek"
print(f'My name is {my_name}, I live in {my_city}, and I am {my_age} years old')

# 🔴 HARD:
# Ask the user for their name and age using input()
# Print a formatted introduction.
name = input('Please enter your full name: ')
age = input('Please enter your age: ')

print(f'My name is {name}, I am {age} years old.')


print("\n=== SECTION 2: DATA TYPES & STRING MANIPULATION ===")

price = 49.99
quantity = 3

# 🟢 EASY:
# Print the total cost.
print(price * quantity)

# 🟡 MEDIUM:
# Print: "Total cost: R___"
print(f'Total cost: R {price * quantity}')


# 🔴 HARD:
# Round to 2 decimal places and format as currency.
print(f'Total: R {round(price * quantity, 2)}')


print("\n=== SECTION 3: CONTROL FLOW ===")

temperature = 18

# 🟢 EASY:
# If temperature > 25 print "Hot" else print "Cold"
if temperature > 25:
    print("Hot")
else:
    print("Cold")


# 🟡 MEDIUM:
# Add "Comfortable" for 15–24
if temperature < 15:
    print("Cold")
elif temperature > 15 and temperature < 24:
    print("Comfortable")
elif temperature > 25:
    print("Hot")



# 🔴 HARD:
# Ask the user for temperature input and classify it.
temp_input = int(input('Please enter the temperature: '))

if temp_input < 15:
    print('Cold')
elif temp_input > 15 and temp_input < 24:
    print('Comfortable')
elif temp_input > 25:
    print('Hot')


print("\n=== SECTION 4: LOGICAL OPERATORS ===")

age = 19
has_ticket = True
is_member = False

# 🟢 EASY:
# Allow entry if age >= 18
if age >= 18:
    print("Entry approved")
else:
    print('Entry Denied') 

# 🟡 MEDIUM:
# Allow entry if age >= 18 AND has_ticket
if age >= 18 and has_ticket:
    print("Entry approved")
else:
    print('Entry Denied') 

# 🔴 HARD:
# Allow entry if age >= 18 AND (has_ticket OR is_member)
if age >= 19 and (has_ticket or is_member):
    print('Entry Approved')
else:
    print('Entry Denied') 


print("\n=== SECTION 5: LISTS ===")

expenses = [120, 75, 90, 45]

# 🟢 EASY:
# Print the list.
print(expenses)

# 🟡 MEDIUM:
# Add a new expense and print total.
expenses.append(60)
print(expenses)

# 🔴 HARD:
# Print total, highest expense, and average.
print(f'Total: {sum(expenses)}')
print(f'Highest: {max(expenses)}')
print(f'Average: {sum(expenses) / len(expenses)}')


print("\n=== SECTION 6: LOOPS ===")

numbers = [3, 7, 10, 2, 8]

# 🟢 EASY:
# Print each number.
for num in numbers:
    print(num)

# 🟡 MEDIUM:
# Print each number and whether it is Even or Odd.
for num in numbers:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

# 🔴 HARD:
# Count how many even numbers exist.
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f'Total Even Numbers: {even_count}')


print("\n=== SECTION 7: DICTIONARIES ===")

employee = {
    "name": "Thabo",
    "department": "Finance",
    "salary": 25000
}

# 🟢 EASY:
# Print the employee name.
print(employee["name"])

# 🟡 MEDIUM:
# Increase salary by 10% and print it.
employee['salary'] = employee["salary"] + employee["salary"] * 0.1
print(f'New Salary: {employee['salary']}')

# 🔴 HARD:
# Add a new key "bonus" and compute total pay.
bonus_percentage = 0.2 
employee["bonus"] = employee["salary"] * bonus_percentage
print(employee)
print(f'Total Pay: {employee["salary"] + employee["bonus"]}')


print("\n=== SECTION 8: NESTING ===")

company = {
    "employee": {
        "name": "Sara",
        "skills": ["Python", "SQL", "Excel"]
    }
}

# 🟢 EASY:
# Print the employee name.
print(company["employee"]["name"])

# 🟡 MEDIUM:
# Print the first skill.
print(company["employee"]["skill"][0])

# 🔴 HARD:
# Print all skills using a loop.
for skill in company["employee"]["skills"]:
    print(skill)


print("\n=== SECTION 9: FUNCTIONS ===")

# 🟢 EASY:
# Create a function that prints "Welcome!"
def welcome():
    print('Welcome!')

# 🟡 MEDIUM:
# Create a function that greets a person by name.
def greet_by_name():
    name_input = input('Enter Your Name: ')
    print(name_input)

greet_by_name()
# 🔴 HARD:
# Create a function that greets a person and tells them the length of their name.
name_input = input('Enter Your Name: ')
def greeting(name_input):
    print(f'Your name {name_input}, is {len(name_input)} characters long.')

greeting(name_input)


print("\n=== SECTION 10: FUNCTIONS WITH OUTPUT ===")

# 🟢 EASY:
# Create a function that adds two numbers.
def add_numbers(num_1, num_2):
    print(f'Sum {num_1 + num_2}')


num_1 = input('Enter the first number: ')
num_2 = input('Enter the first number: ')

add_numbers(num_1=num_1, num_2=num_2)


# 🟡 MEDIUM:
# Return the result instead of printing it.
def add_numbers(num_1, num_2):
    return num_1 + num_2

print(add_numbers(num_1, num_2))


# 🔴 HARD:
# Create a function that calculates final price including 15% VAT.
def final_price(price):
    return int(price) * 0.15

price_input = input('Enter the price: ')
calculated_price = final_price(price_input)
print(f'Final Price: {calculated_price}')


print("\n=== SECTION 11: DEBUGGING ===")

total = 0
prices = [10, 20, 30]

# for price in prices:
#     total = total + price

# print("Total is " + total)  # fix this



# 🔴 HARD:
# Modify code so it handles an empty list safely.
# Updated Code
if len(prices) != 0:
    for price in prices:
        total = total + price

print(f'Total is: {total}')