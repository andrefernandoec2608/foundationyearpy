# ---------------------------
# 🌀 TUPLE
# ---------------------------
# ✅ Understanding tuples and their operations in Python

# 1️⃣ Creating tuples
empty_tuple = ()
single_tuple = (5,)              # single element needs a comma!
mixed_tuple = (10, 3.14, "hello")
print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_tuple)
print("Mixed tuple:", mixed_tuple)


# 2️⃣ Accessing elements
print("First element:", mixed_tuple[0])
print("Last element:", mixed_tuple[-1])


# 3️⃣ #NotaResumen: Example - tuples cannot be changed (immutability)
# Tuples are immutable → you cannot modify their elements
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10   # ❌ TypeError: 'tuple' object does not support item assignment
print("Tuples are immutable, modification is not allowed!")


# 4️⃣ #NotaResumen: Concatenation and repetition of tuples
tuple_a = (1, 2, 3)
tuple_b = (4, 5)
print("Concatenation:", tuple_a + tuple_b)   # (1, 2, 3, 4, 5)
print("Repetition:", tuple_b * 2)            # (4, 5, 4, 5)


# 5️⃣ Tuple packing and unpacking
# Packing → grouping values into one tuple
packed_tuple = ("Alice", 25, "Hungary")
print("Packed tuple:", packed_tuple)

# #NotaResumen: Tuple unpacking
# Unpacking → assigning tuple elements to multiple variables
name, age, country = packed_tuple
print("Unpacked values:", name, age, country)


# 6️⃣ Swapping variables using tuple unpacking
x = 10
y = 20
print("Before swap:", x, y)
(x, y) = (y, x)
print("After swap:", x, y)


# 7️⃣ Membership test
letters = ('a', 'b', 'c')
if 'o' not in letters:
    print("'o' is not in tuple")
else:
    print("'o' found in tuple")


# 8️⃣ Comparing lists vs tuples
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("List:", my_list)
print("Tuple:", my_tuple)

# Lists can change
my_list[0] = 99
print("Modified list:", my_list)

# Tuples cannot
# my_tuple[0] = 99  # ❌ TypeError
print("Tuples are immutable ✅")