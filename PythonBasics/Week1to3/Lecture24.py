# ---------------------------
# 🌀 LISTS & TUPLES — KEY CONCEPTS SUMMARY
# ---------------------------


# 2️⃣ NEGATIVE INDEXING
# Negative indices count from the end of the list:
# -1 → last element, -2 → second to last, and so on.
m_l = [3, 1, -1]
m_l[-2] = m_l[-1]  # replace the second-to-last element with the last
print("Negative indexing example:", m_l)
# Output: [3, -1, -1]


# 3️⃣ LIST REPETITION WITH *
# Multiply a list by an integer to repeat its elements.
lst = [0]
lst = lst * 10
print("List repetition:", lst)
# Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# ⚠️ Be careful: if the list contains mutable objects (like other lists),
# all copies will point to the same inner object (aliasing inside).


# 4️⃣ TUPLE CONCATENATION
t1 = (1, 2, 3)
t2 = (4,)  # single-element tuple → must include the comma
print("Tuple concatenation:", t1 + t2)
# Output: (1, 2, 3, 4)

# ⚠️ Without the comma, (4) would just be an integer, not a tuple.


# 5️⃣ TUPLE INDEXING AND SLICING
my_tup = (1, 2, 3)
print("Access element:", my_tup[2])    # 3rd element
print("Reverse tuple:", my_tup[::-1])  # reverse order
# Output:
# Access element: 3
# Reverse tuple: (3, 2, 1)

# ✅ Tuples support indexing and slicing like lists,
# but they are IMMUTABLE (cannot be changed).


# 6️⃣ TUPLE UNPACKING
tup = (1, 2, 3)
a, b, c = tup  # unpack each element into its variable
print("Tuple unpacking:", a * b * c)
# Output: 6

# You can also pack multiple values into a tuple implicitly
packed = 10, 20, 30   # parentheses are optional
print("Packed tuple:", packed)
# Output: (10, 20, 30)

# Or unpack selectively using the star operator (*)
x, *y = (1, 2, 3, 4, 5)
print("x:", x)
print("y:", y)
# Output:
# x: 1
# y: [2, 3, 4, 5]