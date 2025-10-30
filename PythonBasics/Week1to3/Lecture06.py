# ---------------------------
# 🌀 STRUCTURING PROGRAMS - FUNCTIONS, CLASSES, MODULES
# ---------------------------

# ===========================
# 🌀 FUNCTIONS
# ===========================
print("\n\n🚀 FUNCTIONS")

# 1️⃣ A function is a reusable piece of code.
# It helps to abstract and decompose logic into smaller, clear parts.
# Functions can take inputs (parameters) and return outputs.
# There are two main types of functions:

def greet(name):
    # Function that greets a person by name. It is no a return statement.
    print("Hello,", name)

def add(a, b):
    # Return the sum of two numbers. It is a return statement.
    return a + b

"""
💡 NOTE: Last functions can be rewritten like:

def add(a: int, b: int) -> int:
    return a + b

def show_message() -> None:
    print("Hello!")

It’s not necessary to include ->, but it’s considered a good practice in
professional code — especially in AI, backend, or university projects — because 
it shows intention and clarity.
"""

# 2️⃣ Function calls 
greet("Alice")

result = add(10, 5)
print("Result:", result)

# ===========================
# 🌀 CLASSES
# ===========================
print("\n\n🚀 CLASSES")

# A class groups data (attributes) and behavior (methods) together.

class Person:
    # ---- Class attribute ----
    species = "Human"

    def __init__(self, name: str, age: int, country: str):
        # ---- Instance attributes ----
        self.name = name
        self.age = age
        self.country = country

    # ---- Instance method ----
    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating objects
p1 = Person("Alice", 25, "Hungary")
p2 = Person("Bob", 30, "Germany")

# Using methods
p1.greet()
p2.greet()

# Accessing class and instance attributes
print("Species:", p1.species, p2.species)

# ---- Dynamic attribute (created at runtime) ----
p1.email = "alice@example.com"   # dynamic attribute
print("Dynamic attribute (email):", p1.email)

# ===========================
# 🌀 MODULES
# ===========================
print("\n\n🚀 MODULES")

# Imagine we have another file called "math_utils.py" with functions like this:
# (In a real project, this would be a separate file.)

# ---- math_utils.py ----
# def square(x):
#     return x * x
#
# def cube(x):
#     return x ** 3

# We can import it and use it in another Python file
# import math_utils
#
# print(math_utils.square(4))
# print(math_utils.cube(2))