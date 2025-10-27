# ---------------------------
# 🌀 OBJECT & SCALAR AND NON-SCALAR
# ---------------------------

# 1️⃣ Scalar objects: represent single atomic values
# Think: “one single piece of data”
age = 30          # int
pi = 3.1415       # float
is_student = True # bool
name = "Alice"    # str

print(type(age))       # <class 'int'>
print(type(pi))        # <class 'float'>
print(type(is_student))# <class 'bool'>
print(type(name))      # <class 'str'>

# 2️⃣ Non-scalar objects: represent collections or structures
# Think: “containers of data”.
numbers = [1, 2, 3, 4]                   # list
coordinates = (10, 20)                   # tuple
person = {"name": "Alice", "age": 30}    # dict
unique_numbers = {1, 2, 3, 3, 2}         # set (duplicates removed)

print(type(numbers))       # <class 'list'>
print(type(coordinates))   # <class 'tuple'>
print(type(person))        # <class 'dict'>
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