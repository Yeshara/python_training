# ============================================================

# PYTHON FUNDAMENTALS — LIVE DEMO SCRIPT

# ============================================================

# ── INTRO: Hello World ───────────────────────────────────────



name =''
print(f"Hello, {name}!")

# ── MODULE 1: Variables & Data Types ────────────────────────

print("\n" + "=" * 45)
print("  MODULE 1: Variables & Data Types")
print("=" * 45)

# Basic variables

name   = "Alice"
age    = 30
height = 1.68
active = True

print(name)
print(age)
print(height)
print(active)
print(type(name))
print(type(age))

# Arithmetic

a, b = 10, 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333…
print(a // b)   # 3  (floor division)
print(a % b)    # 1  (remainder)
print(a ** b)   # 1000 (power)

# String operations

first = "Hello"
last  = "World"
print(first + " " + last)   # Hello World
print(first * 3)             # HelloHelloHello
print(len(first))            # 5

# Type conversion

age_text = "25"
print(int(age_text) + 5)    # 30
print(float("3.14"))         # 3.14
print(str(100))              # "100"

# ── MODULE 2: Control Flow ───────────────────────────────────

print("\n" + "=" * 45)
print("  MODULE 2: Control Flow")
print("=" * 45)

# if / elif / else

temperature = 38
if temperature > 37.5:
    print("You have a fever!")
elif temperature >= 36.1:
    print("Normal temperature")
else:
    print("Temperature is low")
# Boolean logic

age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("Welcome to the show!")

if not has_ticket:
    print("Please buy a ticket")

# for loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  - {fruit}")

# range()

for i in range(1, 6):
    print(i, end=" ")
print()

# while loop

count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# FizzBuzz

for n in range(1, 16):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# ── MODULE 3: Functions ──────────────────────────────────────

print("\n" + "=" * 45)
print("  MODULE 3: Functions")
print("=" * 45)

# Basic function

def say_hello():
    print("Hello from a function!")

say_hello()
say_hello()

# Parameters

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# Default parameter

def greet_formal(name, title="Ms"):
    print(f"Good morning, {title} {name}.")

greet_formal("Smith")
greet_formal("Jones", "Dr")

# Return values

def add(a, b):
    return a + b

print(add(5, 3))       # 8
print(add(10, 20))     # 30

# Practical function

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

for temp in [0, 20, 37, 100]:
print(f"  {temp}°C = {celsius_to_fahrenheit(temp)}°F")

# ── MODULE 4: Lists, Dicts & Tuples ─────────────────────────

print("\n" + "=" * 45)
print("  MODULE 4: Lists, Dicts & Tuples")
print("=" * 45)

# Lists

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])      # apple
print(fruits[-1])     # date
print(fruits[1:3])    # [‘banana’, ‘cherry’]
print(len(fruits))    # 4

fruits.append("elderberry")
fruits.remove("banana")
fruits.sort()
print(fruits)

# Dictionaries

person = {
    "name": "Alice",
    "age":  30,
    "city": "London"
}
print(person["name"])
print(person.get("email", "No email on file"))

person["email"] = "alice@example.com"
for key, value in person.items():
    print(f"  {key}: {value}")

# Tuples

coordinates = (51.5074, -0.1278)
lat, lng = coordinates
print(f"Lat: {lat}, Lng: {lng}")

# ── MODULE 5: Loops, Nesting & Debugging ────────────────────

print("\n" + "=" * 45)
print("  MODULE 5: Loops, Nesting & Debugging")
print("=" * 45)

# — List comprehensions: compact loops —

print("– List comprehensions –")

squares = [x ** 2 for x in range(1, 6)]
print(squares)                          # [1, 4, 9, 16, 25]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)                            # [2, 4, 6, 8, 10]

names = ["alice", "bob", "charlie"]
upper_names = [n.upper() for n in names]
print(upper_names)                      # [‘ALICE’, ‘BOB’, ‘CHARLIE’]

# — Nested loops —

print("\n– Nested loops –")

# Multiplication table (3x3)

for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:>4}", end="")
    print()                             # newline after each row

# Nested loop over a list of lists

classroom = [
["Alice", "Bob"],
["Charlie", "Diana"],
["Eve", "Frank"],
]
for group_num, group in enumerate(classroom, start=1):
    print(f"Group {group_num}:", end=" ")
    for student in group:
        print(student, end=" ")
    print()

# — Nested data structures —

print("\n– Nested data structures –")

library = {
"fiction":     ["1984", "Brave New World", "Fahrenheit 451"],
"non-fiction": ["Sapiens", "Thinking Fast and Slow"],
"science":     ["A Brief History of Time", "The Selfish Gene"],
}

for genre, books in library.items():
    print(f"\n{genre.upper()}:")
    for i, book in enumerate(books, start=1):
        print(f"  {i}. {book}")

# — Debugging techniques —

print("\n– Debugging –")

# 1. Print statements to trace values

def calculate_discount(price, discount_pct):
    print(f"  [DEBUG] price={price}, discount_pct={discount_pct}")  # trace inputs
    discount = price * (discount_pct / 100)
    print(f"  [DEBUG] discount={discount}")                          # trace intermediate
    final = price - discount
    return final

total = calculate_discount(120, 15)
print(f"Final price: £{total}")

# 2. type() and isinstance() to catch type errors early

print("\n– Type checking –")
values = [42, "hello", 3.14, True, [1, 2, 3]]
for v in values:
    print(f"  {str(v):<12} → type: {type(v).__name__}")

# 3. Common errors and what they mean

print("\n– Common errors (caught with try/except) –")

# NameError

try:
    print(undefined_variable)
except NameError as e:
    print(f"  NameError: {e}")

# TypeError

try:
    result = "age: " + 25
except TypeError as e:
    print(f"  TypeError: {e}")

# IndexError

try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    print(f"  IndexError: {e}")

# KeyError

try:
    person = {"name": "Alice"}
    print(person["email"])
except KeyError as e:
    print(f"  KeyError: {e}")

# ZeroDivisionError

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"  ZeroDivisionError: {e}")

# 4. assert — sanity-check assumptions while developing

print("\n– assert statements –")

def divide(a, b):
    assert b != 0, "Denominator cannot be zero!"
    return a / b

print(divide(10, 2))    # 5.0
try:
    print(divide(10, 0))
except AssertionError as e:
    print(f"  AssertionError: {e}")

# ── GRAND CHALLENGE: Student Grade Manager ───────────────────

print("\n" + "=" * 45)
print("  GRAND CHALLENGE: Grade Manager")
print("=" * 45)

students = {
"Alice":   [88, 92, 79],
"Bob":     [74, 68, 82],
"Charlie": [95, 97, 91],
"Diana":   [61, 55, 70],
"Eve":     [83, 88, 90],
}

def get_average(scores):
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:   return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else:               return "Fail"

print(f"{‘Student’:<10} {‘Avg’:>6} {‘Grade’:>6}")
print("-" * 26)

all_averages = []
for name, scores in students.items():
    avg   = get_average(scores)
    grade = get_grade(avg)
    all_averages.append(avg)
    print(f"{name:<10} {avg:>6.1f} {grade:>6}")

print("-" * 26)
print(f"Class avg:  {get_average(all_averages):.1f}")

top_idx  = all_averages.index(max(all_averages))
top_name = list(students.keys())[top_idx]
print(f"Top student: {top_name}")