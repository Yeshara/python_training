#Exercise 1

Name = input("Please enter your name: ")
Age = input("Please enter your age: ")
print(f"Hello, my name is {Name} and I am {Age} years old.")

#Exercise 2
price = 49.99
quantity = 3

Total_cost=price*quantity

print(f"Total cost: R{Total_cost:.2f}")

print("\n=== SECTION 5: LISTS ===")

expenses = [120, 75, 90, 45]

# 🟢 EASY:
# Print the list.
print(expenses)

# 🟡 MEDIUM:
# Add a new expense and print total.

expenses.append(36)
print(expenses)

# 🔴 HARD:
# Print total, highest expense, and average.

Total=sum(expenses)
Highest=max(expenses)
Average=Total/len(expenses)

print(f"Total: {Total}")
print(f"Highest expense: {Highest}")
print(f"Average: {Average}")


print("\n=== SECTION 6: LOOPS ===")

numbers = [3, 7, 10, 2, 8]

# 🟢 EASY:
# Print each number.
for i in numbers:
    print(i)

# 🟡 MEDIUM:
# Print each number and whether it is Even or Odd.

for i in numbers:
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")          

# 🔴 HARD:
# Count how many even numbers exist.

even_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1

print(f"Total even numbers: {even_count}")


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

employee["bonus"] = 10000 
total_pay = employee["salary"] + employee["bonus"]
print(f"Total pay : {total_pay}")




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

for AllSkills in company["employee"]["skills"]:
    print(AllSkills)
