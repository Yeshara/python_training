#SECTION 1

name = input("Please enter your name: ")
age = input("Please enter your age: ")


print(f"Hello, my name is {name} and I am {age} years old.")

#SECTION 2
price = 49.99
quantity = 3

total = price * quantity

formatted_total = f"£{total:.2f}"

print(f"The total price is {formatted_total}")



#Section 3 

temperature = float(input("Enter the temperature in °C: "))


if temperature < 10:
    classification = "cold"
elif 10 <= temperature < 25:
    classification = "warm"
else:
    classification = "hot"

print(f"The temperature is {temperature}°C, which is considered {classification}.")
