# ---------------------------
# 🌀 STRINGS IN PYTHON
# ---------------------------
# Strings are sequences of characters.
# They are immutable, meaning you cannot change them in place.

# Example string
str1 = "hello"

# 1️⃣ Indexing
print("\n\n🚀 Indexing")
print(str1[0])   # 'h'  -> first character
print(str1[-1])  # 'o'  -> last character (negative index counts from the end)

# 2️⃣ Slicing
print("\n\n🚀 Slicing")
# Syntax: string[start:stop:step]
print(str1[1:4])   # 'ell'   -> from index 1 up to (not including) 4
print(str1[0:])    # 'hello' -> from index 0 to the end
print(str1[::-1])  # 'olleh' -> reversed string

# 3️⃣ Immutability
print("\n\n🚀 Immutability")
# Strings cannot be changed directly.
# The following line will raise an error:
# str1[0] = 'y'   # ❌ TypeError: 'str' object does not support item assignment

# 4️⃣ Instead, create a new string
print("\n\n🚀 Instead, create a new string")
str4 = 'y' + str1[1:]
print(str4)   # 'yello'

# 5️⃣ String length
print("\n\n🚀 String length")
print(len(str4))   # 5  -> number of characters in the string