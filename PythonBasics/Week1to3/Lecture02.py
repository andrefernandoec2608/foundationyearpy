# ---------------------------
# 🌀 OBJECT & SCALAR AND NON-SCALAR
# ---------------------------

# 1️⃣ Scalar objects: represent single atomic values (atomic values; immutable)
# Think: “one single piece of data”
age = 30          # int
pi = 3.1415       # float
is_student = True # bool
name = "Alice"    # str (immutable, hashable, iterable)
nothing = None    # NoneType (represents absence; immutable)

print(type(age))       # <class 'int'>
print(type(pi))        # <class 'float'>
print(type(is_student))# <class 'bool'>
print(type(name))      # <class 'str'>
print(type(nothing))   # <class 'NoneType'>

# 2️⃣ Non-scalar objects: represent collections or structures (composite structures; may be mutable)
# Think: “containers of data”.

# LIST — ordered, mutable
numbers = [1, 2, 3, 4]
numbers[0] = 11         # we can change elements in a list
numbers.append(5)       # we can add elements to a list
numbers.remove(3)       # we can remove elements from a list

print(type(numbers))    # <class 'list'>

# DICT — mapping (key → value), mutable; keys must be hashable (immutable)
person = {"name": "Alice","age": 30,"city": "Budapest"}
person["age"] = 31              # we can update existing keys 
person["country"] = "Hungary"   # we can add new key-value pairs
del person["city"]              # we can remove key-value pairs

print(type(person))             # <class 'dict'>

"""
💡 NOTE:
Keys ("name", "age", "city") must be immutable (strings, ints, immutable tuples, etc.).
Values ​​can be of any type (including lists, other dictionaries, or functions).
"""

# TUPLE — It is like a list, but immutable (cannot be changed after creation)
coords = (10, 20, 30)
# coords[1] = 25  → TypeError   # we cannot change elements in a tuple
new_coords = coords + (40,)     # we can create a new tuple by concatenation

print(type(coords))             # <class 'tuple'>

# SET — unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 3, 2}   # duplicates are automatically removed
print(unique_numbers)              # {1, 2, 3}
unique_numbers.add(3)              # o change (duplicates ignored)
print(unique_numbers)              # {1, 2, 3}
unique_numbers.add(4)              # adding a new value
print(unique_numbers)              # {1, 2, 3, 4}
unique_numbers.update({5, 6})      # add multiple elements
print(unique_numbers)              # {1, 2, 3, 4, 5, 6}
unique_numbers.update({3, 4, 7})   # 3 and 4 are duplicates and be ignored; only 7 is new
print(unique_numbers)              # {1, 2, 3, 4, 5, 6, 7}

print(type(unique_numbers))# <class 'set'>

# 🌀 EXTRA knowledge: Basic arithmetic operations
a = 5
b = 2

print(a + b)   # 7   (addition)
print(a * b)   # 10  (multiplication)
print(a - b)   # 3   (subtraction)
print(a / b)   # 2.5 (normal division, float)
print(a // b)  # 2   (floor division, integer part)
print(a % b)   # 1   (modulo, remainder)
print(a ** 2)  # 25  (power: 5 squared)
print(a ** b)  # 25  (power: 5 to the power of 2)