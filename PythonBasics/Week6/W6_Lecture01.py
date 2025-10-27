# ---------------------------
# 🌀 CLASS DEFINITION & INITIALIZATION
# ---------------------------

# A class defines a new data type that groups data (attributes) and behavior (methods).
# In Python, every class implicitly inherits from 'object'.

# Basic syntax:
class Person(object):
    # It runs automatically when you create a new instance.
    def __init__(self, name, age):
        # 'self' refers to the specific instance being created.
        self.name = name
        self.age = age
"""
NOTE: Internally, Python:
Calls Person.__new__() to allocate memory.
Then executes Person.__init__(p1, "Alice", 22) to initialize it
"""

# Creating objects (instances)
p1 = Person("Alice", 22)
p2 = Person("Bob", 30)

# Accessing attributes through dot notation
print(p1.name)   # Alice
print(p2.age)    # 30

# Each instance has its own independent data
p1.age = 23
print(p1.age)    # 23
print(p2.age)    # 30

# -----------------------------------
# SELF PARAMETER
# -----------------------------------

# 'self' is the reference to the current object (like 'this' in Java).
# You never pass it manually when calling a method — Python does it for you.

class Student:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hi, I'm {self.name}!")

s1 = Student("Luna")
s1.say_hello()       # Python internally calls: Student.say_hello(s1)

# Equivalent manual call (rarely used but valid):
Student.say_hello(s1)  # -> Hi, I'm Luna!

# -----------------------------------
# DEFAULT ARGUMENTS
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

# ⚠️ Avoid mutable defaults (like lists or dicts):
# Bad example:
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

# -----------------------------------
# DYNAMIC ATTRIBUTE CREATION
# -----------------------------------

# You can create new attributes from outside the class definition:
p1.country = "Hungary"
print(p1.country)   # Hungary

# This flexibility is powerful but should be used carefully:
# it can make your objects inconsistent if overused.

# -----------------------------------
# TYPE CHECKS
# -----------------------------------
print(isinstance(p1, Person))  # True
print(isinstance(p1, object))  # True