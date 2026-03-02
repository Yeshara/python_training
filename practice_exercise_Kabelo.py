#Section 3

# 🟢 EASY
#temperature = 23

#if temperature > 25:
#    print("Hot")
#else: 
 #   print("Cold")

 # 🟡 MEDIUM:
# Add "Comfortable" for 15–24

#if temperature > 25:
#    print("Hot")
#elif temperature >= 15 and temperature <= 24:
#    print('Comfortable')
#else:
 #   print("Cold")


# 🔴 HARD:
# Ask the user for temperature input and classify it.
# temp = int(input("Please input the temperature: "))
# if temp > 25:
#     print("Hot")
# elif temp > 15 and temp <= 24:
#     print("Comfortable")
# else:
#     print("Cold")






# print("\n=== SECTION 4: LOGICAL OPERATORS ===")

age = 19
has_ticket = True
is_member = False

# 🟢 EASY:
# Allow entry if age >= 18
if  age >= 18:
 print("Entry Granted!!")
else:
   print("Access Denied, Go grow up")


# 🟡 MEDIUM:
# Allow entry if age >= 18 AND has_ticket
if age >= 18 and has_ticket:
 print("Entry Granted!! Again")
else:
   print("Access Denied, Go grow up")


# 🔴 HARD:
# Allow entry if age >= 18 AND (has_ticket OR is_member)
if age >= 18 and (has_ticket or is_member):
    print("Entry Granted!! Again and Again")
else:
    print("Access Denied, Go grow up")
