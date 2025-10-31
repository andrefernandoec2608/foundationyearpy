# -----------------------------------
# 🌀 DEFAULT ARGUMENTS
# -----------------------------------

# Default arguments allow you to specify default values for parameters in methods.
# If the caller does not provide a value for that parameter, the default is used.
# This is particularly useful in __init__ methods of classes.

# You can define default parameter values in __init__:
class Car:
    def __init__(self, brand, year=2020):
        self.brand = brand
        self.year = year

c1 = Car("Tesla")
c2 = Car("BMW", 2022)

print(c1.year)   # 2020 (default value)
print(c2.year)   # 2022

# ⚠️ ALERT: Avoid mutable defaults (like lists or dicts):
# If you use a mutable object as a default value, it will be shared across all instances of the class.
# This can lead to unexpected behavior.
# Example:
class Bag:
    def __init__(self, items=[]):
        self.items = items

b1 = Bag()
b2 = Bag()

b1.items.append("Book")
print(b2.items)  # ['Book']  -> shared list! (⚠️ ALERT: dangerous!)

# 🌀 EXTRA knowledge: Correct approach
# Use None as the default value and create a new list inside the method:
class SafeBag:
    def __init__(self, items=None):
        self.items = [] if items is None else list(items)
