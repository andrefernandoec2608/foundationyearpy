# ---------------------------
# 🌀 Strings in Python
# ---------------------------

# Strings are sequences of characters.
# They are immutable, meaning you cannot change them in place.

str1 = "hello"

# --- Indexing ---
print(str1[0])   # 'h'  -> first character
print(str1[-1])  # 'o'  -> last character (negative index counts from the end)

# --- Slicing ---
# Syntax: string[start:stop:step]
print(str1[1:4])   # 'ell'   -> from index 1 up to (not including) 4
print(str1[0:])    # 'hello' -> from index 0 to the end
print(str1[::-1])  # 'olleh' -> reversed string

# --- Immutability ---
# Strings cannot be changed directly.
# The following line will raise an error:
# str1[0] = 'y'   # ❌ TypeError: 'str' object does not support item assignment

# Instead, create a new string
str4 = 'y' + str1[1:]
print(str4)   # 'yello'

# --- String length ---
print(len(str4))   # 5  -> number of characters in the string