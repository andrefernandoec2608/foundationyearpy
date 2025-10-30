# ---------------------------
# 🌀 F-STRINGS (FORMATTED STRING LITERALS)
# ---------------------------
#  Available in Python 3.6 and later
#  Syntax: f"Your text {variable} more text {expression}"
#  Used for embedding expressions inside string literals

# Basic example: inserting variables inside a string
name = "Alice"
age = 25
country = "Hungary"

# f-string automatically replaces {variables} with their values
print(f"My name is {name}, I am {age} years old, and I live in {country}.")

# ---------------------------
# Using expressions inside {}
# ---------------------------

a = 10
b = 5

# You can directly perform calculations inside the f-string
print(f"The sum of {a} and {b} is {a + b}.")
print(f"The product of {a} and {b} is {a * b}.")
print(f"{a} divided by {b} equals {a / b}.")

# ---------------------------
# Using function calls inside {}
# ---------------------------

def greet(person):
    # Convert the name to uppercase using .upper()
    return f"Hello, {person.upper()}! Welcome to Python."

# Calling the function inside another f-string
print(f"Greeting message: {greet(name)}")

# ---------------------------
# 🌀 Formatting numbers in f-strings
# (optional but useful for later)
# ---------------------------

pi = 3.1415926535
print(f"Pi rounded to 2 decimals: {pi:.2f}")  # .2f means 2 decimal places
print(f"Pi as percentage: {pi:.2%}")          # format as percentage