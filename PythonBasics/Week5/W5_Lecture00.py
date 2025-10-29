# ---------------------------
# 🌀 CLASSES AND INSTANCES
# ---------------------------

# A class is a "blueprint" that defines attributes (data) and methods (behavior).
# When you call a class like a function, you create (instantiate) a new object.

class Student:
    def __init__(self, name):
        # 'self' refers to the specific instance being created
        self.name = name

# Creating instances
s1 = Student("Alice")
s2 = Student("Bob")

# Each instance has its own data stored inside the 'self' namespace
print(s1.name)   # Alice
print(s2.name)   # Bob

# -----------------------------------
# DOT NOTATION
# -----------------------------------

# The '.' operator is used to access:
#   • data attributes  -> s1.name
#   • methods           -> s1.some_method()

# You can also create new attributes dynamically (Python allows it!)
# BUT it is not good practice for formal classes
s1.age = 21
print(s1.age)    # 21

# s2 doesn't have 'age' because we added it only to s1
# print(s2.age)  # -> AttributeError

"""
💡NOTE: This flexibility is powerful but should be used carefully:
it can make your objects inconsistent if overused.
"""

# -----------------------------------
# TYPE AND ISINSTANCE
# -----------------------------------

print(type(s1))                     # <class '__main__.Student'>
print(isinstance(s1, Student))      # True
print(isinstance(s1, object))       # True (because all classes inherit from object)

# -----------------------------------
# CLASSES ARE OBJECTS TOO
# -----------------------------------

# In Python, a class is itself an object of type 'type'.
print(type(Student))   # <class 'type'>

"""
💡NOTE:  So 'Student' is an instance of 'type', and 's1' is an instance of 'Student'.
(This is part of Python’s dynamic object model.)
"""

# -----------------------------------
# EVERYTHING IS AN OBJECT
# -----------------------------------

# In Python, everything is an object — numbers, strings, functions, even classes themselves.
# Each object has:
#   • identity   -> unique id() in memory
#   • type       -> returned by type()
#   • value      -> the data it holds

# Example 1: Basic built-in objects
x = 42
y = "hello"

#TYPE
print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>
#IDENTITY
print(id(x))     # unique memory id
print(id(y))     # unique memory id
#VALUE
print(x)         # 42
print(y)         # hello

# -----------------------------------
# 🌀 EXTRA knowledge: IDENTITY vs EQUALITY
# -----------------------------------

# 'is' checks if two variables point to the SAME object in memory
# '==' checks if two objects have the SAME value (via __eq__)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  -> same value
print(a is b)   # False -> different memory locations