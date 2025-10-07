# ---------------------------
# LIST COPYING, SLICING & ALIASING SUMMARY
# ---------------------------

# 1️⃣ Aliasing (same object in memory)
# Two variables reference the SAME list (no copy)
list_a = ["A", "B", "C"]
list_b = list_a   # aliasing: both names point to the same object

list_b[0] = "Z"   # modify through one alias
print("list_a:", list_a)
print("list_b:", list_b)

# Output:
# list_a: ['Z', 'B', 'C']
# list_b: ['Z', 'B', 'C']

# Visual model:
# ┌──────────────────┐
# │ ['Z','B','C']    │
# └──────────────────┘
#   ↑       ↑
# list_a   list_b


# 2️⃣ Cloning / Copying a list (independent object)
# Use slicing [:] to make a shallow copy
list_1 = ["A", "B", "C"]
list_2 = list_1[:]   # new list object
list_3 = list_2[:]   # another new list

del list_1[0]        # remove first element from list_1
del list_2[:]        # empty list_2 only

print("list_1:", list_1)  # ['B', 'C']
print("list_2:", list_2)  # []
print("list_3:", list_3)  # ['A', 'B', 'C']

# Visual model:
# ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
# │ ['B','C']     │     │ []            │     │ ['A','B','C'] │
# └───────────────┘     └───────────────┘     └───────────────┘
#     ↑                     ↑                     ↑
#   list_1                list_2                list_3

# ✅ Modifying one list does NOT affect the others.


# 3️⃣ Verifying aliasing vs cloning
x = [1, 2, 3]
y = x      # alias
z = x[:]   # clone

print("x is y:", x is y)  # True → same object (alias)
print("x is z:", x is z)  # False → new object (copy)

y[0] = 99
print("x:", x)
print("y:", y)
print("z:", z)
# Output:
# x is y: True
# x is z: False
# x: [99, 2, 3]
# y: [99, 2, 3]
# z: [1, 2, 3]


# 4️⃣ Internal aliasing with nested lists (For advanced knoldge)
matrix = [[1, 2]] * 3
print("Before:", matrix)
matrix[0][0] = 99
print("After:", matrix)

# Output:
# Before: [[1, 2], [1, 2], [1, 2]]
# After:  [[99, 2], [99, 2], [99, 2]]

# ⚠️ All rows refer to the same sublist!
# ┌───────────────┐
# │ [1, 2]        │  ← same inner object used 3 times
# └───────────────┘
#   ↑     ↑     ↑
#  row1 row2  row3

# To create independent sublists:
matrix_fixed = [[1, 2] for _ in range(3)]
print("Independent:", matrix_fixed)
matrix_fixed[0][0] = 99
print("Modified:", matrix_fixed)
# Output:
# Independent: [[1, 2], [1, 2], [1, 2]]
# Modified: [[99, 2], [1, 2], [1, 2]]