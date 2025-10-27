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
# It’s equivalent to Java's dot notation (object.field or object.method()).

# You can also create new attributes dynamically (Python allows it!)
s1.age = 21
print(s1.age)    # 21

# s2 doesn't have 'age' because we added it only to s1
# print(s2.age)  # -> AttributeError

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

# So 'Student' is an instance of 'type', and 's1' is an instance of 'Student'.
# (This is part of Python’s dynamic object model.)
