# -----------------------------------
# 🌀 DEFAULT ARGUMENTS
# -----------------------------------

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
class Bag:
    def __init__(self, items=[]):
        self.items = items

b1 = Bag()
b2 = Bag()

b1.items.append("Book")
print(b2.items)  # ['Book']  -> shared list! (dangerous!)

# Correct approach:
class SafeBag:
    def __init__(self, items=None):
        self.items = [] if items is None else list(items)
