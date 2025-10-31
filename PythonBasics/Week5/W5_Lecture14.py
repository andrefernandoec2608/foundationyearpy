# ---------------------------
# 🌀 type() & class
# ---------------------------
# Python treats everything (even classes) as objects.
# This lecture explores the dual role of type() in Python.

# type() has two main purposes:
# 1) Returns the class of an instance (type(obj)).
# 2) Creates new classes dynamically (type(name, bases, dict)).


# -----------------------------------
# 1️⃣ type() — checking the type of objects
# type() returns the CLASS that created the object.
# -----------------------------------
x = 42
print(type(x))     # <class 'int'>

text = "Hello"
print(type(text))  # <class 'str'>


# -----------------------------------
# 2️⃣ Classes themselves are objects
# -----------------------------------
class Pizza:
    pass

p = Pizza()
print(type(p))       # <class '__main__.Pizza'>   → p is an instance of Pizza
print(type(Pizza))   # <class 'type'>             → Pizza itself is an object of type 'type'

# That means 'type' created the class 'Pizza',
# just like 'Pizza' created the object 'p'.

# -----------------------------------
# 3️⃣ Dynamic class creation with type()
# -----------------------------------
# type(name, bases, dict) → creates a class dynamically at runtime.
DynamicPizza = type(
    "DynamicPizza",          # class name
    (object,),               # base classes (tuple)
    {"bake": lambda self: "DynamicPizza dynamically created pizza! 🍕"}
)

dp = DynamicPizza() # It creates an instance of the dynamic class
print(dp.bake())  # Output: DynamicPizza dynamically created pizza! 🍕

# Equivalent to:
# class DynamicPizza:
#     def bake(self):
#         return "DynamicPizza dynamically created pizza! 🍕"

# -----------------------------------
# 4️⃣ Relationship between 'type' and 'object'
# -----------------------------------
print(isinstance(p, Pizza))        # True  → p is instance of Pizza
print(isinstance(Pizza, type))     # True  → Pizza is instance of type
print(isinstance(type, object))    # True  → type is a subclass of object
print(isinstance(object, type))    # True  → object is created by type

# type and  object form a minimal closed loop:
# object → type → object

"""
💡 NOTE: Summary table

| Element             | Creates             | Instance of   |
|---------------------|--------------------|---------------|
| object (root)       | —                  | type          |
| type                | classes            | type (itself) |
| Your class (Pizza)  | objects            | type          |
| Your object (p)     | —                  | Pizza         |
"""

"""
💡 NOTE: CONCEPT SUMMARY
• A class is an instance of 'type'.
• 'object' is the root of all classes.
• 'type' and 'object' form a circular relationship:
      object is an instance of type,
      and type inherits from object.
"""

"""
💡 NOTE: WHY IT MATTERS
Understanding this is key to:
• metaprogramming (creating/modifying classes dynamically)
• advanced frameworks (ORMs, AI models, dynamic API generation)
"""