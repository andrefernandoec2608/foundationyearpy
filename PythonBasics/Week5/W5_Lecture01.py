# ---------------------------
# 🌀 CLASS DEFINITION & INITIALIZATION
# ---------------------------

# A class defines a new data type that groups data (attributes) and behavior (methods).
# In Python, every class implicitly inherits from 'object'.

# __init__ is an initializer that automatically initializes a new object’s attributes when the class is instantiated.

# Basic syntax of a Class
class Person(object):
    def __init__(self, name, age):
        # 'self' refers to the specific instance being created.
        self.name = name
        self.age = age

"""
💡NOTE: Internally, Python:
Calls Person.__new__() to allocate memory.
Then executes Person.__init__(p1, "Alice", 22) to initialize it
"""

"""
💡NOTE:
(object) is optional in Python 3 and newer,
because every class automatically inherits from object.
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