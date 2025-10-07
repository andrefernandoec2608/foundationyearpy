# ---------------------------
# STRUCTURING PROGRAMS IN PYTHON
# ---------------------------

# ===========================
# 1. FUNCTIONS
# ===========================

# A function is a reusable piece of code.
# It helps to abstract and decompose logic into smaller, clear parts.

def greet(name):
    """Function that greets a person by name"""
    print("Hello,", name)

def add(a, b):
    """Return the sum of two numbers"""
    return a + b

# Function calls
greet("Alice")
result = add(10, 5)
print("Result:", result)

# no return statement
def show_message():
    print("Hello!")   # no return statement
print(show_message())   # prints "Hello!" then returns None

# ===========================
# 2. CLASSES
# ===========================

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
# 3. MODULES
# ===========================

# Imagine we have another file called "math_utils.py" with functions like this:
# (In a real project, this would be a separate file.)

# ---- math_utils.py ----
# def square(x):
#     return x * x
#
# def cube(x):
#     return x ** 3

# We can import and use it in another script:
# import math_utils
# print(math_utils.square(4))
# print(math_utils.cube(2))


# ===========================
# WHY THIS MATTERS
# ===========================

# - Functions → reusable blocks for logic abstraction
# - Classes → organize data and behavior
# - Modules → group related code into files for clarity and scalability

print("Program structured successfully ✅")