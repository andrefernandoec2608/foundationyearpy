# ---------------------------
# 🌀 OBJECT IN PYTHON
# ---------------------------

# In Python, everything is an object — numbers, strings, functions, even classes themselves.
# Each object has:
#   • identity   -> unique id() in memory
#   • type       -> returned by type()
#   • value      -> the data it holds

# Example 1: Basic built-in objects
x = 42
y = "hello"

print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>
print(id(x))     # unique memory id
print(id(y))

# -----------------------------------
# IDENTITY vs EQUALITY
# -----------------------------------

# 'is' checks if two variables point to the SAME object in memory
# '==' checks if two objects have the SAME value (via __eq__)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  -> same value
print(a is b)   # False -> different memory locations