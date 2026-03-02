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


print("\n=== SECTION 3: CONTROL FLOW ===")

temperature = 18

# 🟢 EASY:
# If temperature > 25 print "Hot" else print "Cold"
if(temperature > 25):
    print("Temperature Classification Easy: Hot")
else:
    print("Temperature Classification Easy: Cold")
# 🟡 MEDIUM:
# Add "Comfortable" for 15–24
if(temperature > 25):
    print("Temperature Classification Medium: Hot")
elif (temperature>=15 and temperature<=24): 
    print("Temperature Classification Medium: Comfortable")
else:
    print("Temperature Classification Medium: Cold")
# 🔴 HARD:
# Ask the user for temperature input and classify it.
temperature_celsius = int(input("Please provide the temperature in the room: "))
if(temperature_celsius > 25):
    print("Temperature Classification Hard: Hot")
elif (temperature_celsius>=15 and temperature_celsius<=24): 
    print("Temperature Classification Hard: Comfortable")
else:
    print("Temperature Classification Hard: Cold")

print("\n=== SECTION 4: LOGICAL OPERATORS ===")

age = 19
has_ticket = True
is_member = False

# 🟢 EASY:
# Allow entry if age >= 18
if(age>=18):
    print("Admitted: Is 18+")
else:
    print("Admissions Denied")

# 🟡 MEDIUM:
# Allow entry if age >= 18 AND has_ticket
if(age>=18 and has_ticket):
    print("Admitted: Is 18+ & has a valid ticket")
else:
    print("Admissions Denied")
# 🔴 HARD:
# Allow entry if age >= 18 AND (has_ticket OR is_member)
if(age>=18 and (has_ticket or is_member)):
    print("Admitted: Is 18+. And is either a memeber or has a valid ticket")
else:
    print("Admissions Denied")

print("\n=== SECTION 5: LISTS ===")

expenses = [120, 75, 90, 45]

# 🟢 EASY:
# Print the list.
print(expenses)
print(sum(expenses))
# 🟡 MEDIUM:
# Add a new expense and print total.
expenses.append(55)
total = sum(expenses)
print(total)
# 🔴 HARD:
# Print total, highest expense, and average.
total_expense = 0
highest_expense = 0
average_expense = 0

print(f"Total Expenses Hard: {sum(expenses)}")
print(f"Highest Value in List Hard: {max(expenses)}")
print(f"Average Expense Hard is: {sum(expenses)/len(expenses)}")


print("\n=== SECTION 6: LOOPS ===")

numbers = [3, 7, 10, 2, 8]

# 🟢 EASY:
# Print each number.
for num in numbers:
    print(num)
# 🟡 MEDIUM:
# Print each number and whether it is Even or Odd.
for num in numbers:
    if(num%2==0):
        print(f"Number: {num}; it is EVEN")
    else:
        print(f"Number: {num}; it is ODD")
# 🔴 HARD:
# Count how many even numbers exist.
count_even = 0
for num in numbers:
    if(num%2==0):
        count_even = count_even + 1
print(count_even)


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
employee["salary"] = employee["salary"]*1.1
print(f"{employee["name"]}, increased salary (10%): R{employee["salary"]:,.2f}")
# 🔴 HARD:
# Add a new key "bonus" and compute total pay.
employee["bonus"]=employee["salary"]*0.15
total_pay = employee["salary"]+employee["bonus"]
print(f"Total Pay (Salary and Bonus): R{total_pay:,.2f}")



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
print(company["employee"]["skills"][0])
# 🔴 HARD:
# Print all skills using a loop.
for i in range(len(company["employee"]["skills"])):
    print(company["employee"]["skills"][i])


print("\n=== SECTION 9: FUNCTIONS ===")
# 🟢 EASY:
# Create a function that prints "Welcome!"
def welcome_message():
    print("Welcome!")
# 🟡 MEDIUM:
# Create a function that greets a person by name.
def welcome_person_message(name_user):
    print(f"Welcome {name_user} ! Enjoy")
# 🔴 HARD:
# Create a function that greets a person and tells them the length of their name.
def welcome_person_and_length_message(name_user):
    print(f"Welcome {name_user} ! The length of your name is {len(name_user)}")


print("\n=== SECTION 10: FUNCTIONS WITH OUTPUT ===")
# 🟢 EASY:
# Create a function that adds two numbers.
def add_two_numbers_int(x: int, y:int)->int:
    print(f"Adding 2 integers EASY: R{x+y}")
add_two_numbers_int(6,4)

# 🟡 MEDIUM:
# Return the result instead of printing it.
def add_two_numbers(x: float, y:float)->float:
    return x+y
addition = add_two_numbers(6.5,4.2)
print(f"Adding 2 floats with return MED:{addition}")
# 🔴 HARD:
# Create a function that calculates final price including 15% VAT.
def final_price(price: float,vat_amount: float)->float:
    vat = price*vat_amount
    final_price_value = add_two_numbers(price, vat)
    return final_price_value
price = float(input("Please enter price of good sold: "))
vat_value = float(input("Please enter VAT percentage as decimal (15%->0.15): "))
total_price = final_price(price,vat_value)
print(f"Adding VAT (15%) to final price:{total_price:,.2f}")