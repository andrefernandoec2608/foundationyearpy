# In Python, everything is an object.
# Each object has:
# 1. A Type (what kind of object it is)
# 2. A Value (the data it holds)
# 3. A Behavior (the operations/methods it supports)

# 🌀 Example with an integer
x = 42

# 1. Type
print(type(x))   # <class 'int'>

# 2. Value
print(x)         # 42

# 3. Behavior (calling a method of the int object)
print(x.bit_length())   # 6 -> the number of bits required to represent 42


# 🌀 Example with a string
s = "hello"

# 1. Type
print(type(s))   # <class 'str'>

# 2. Value
print(s)         # "hello"

# 3. Behavior (calling methods of the str object)
print(s.upper())        # "HELLO"
print(s.replace("h", "j"))  # "jello"