# ---------------------------
# 🌀 EQUALITY vs IDENTITY vs MUTABILITY 
# ---------------------------

# Every object in Python has three main properties:
# 1️⃣ Identity  → unique memory address of the object
# 2️⃣ Type      → defines what kind of object it is (int, list, str, etc.)
# 3️⃣ Value     → the data stored inside the object

# You can check the ID (identity) with id(obj)
# and compare identities with the "is" operator.

# You can check equality (same content/value) with the "==" operator.
# It compares the *values* stored inside the objects, not their memory location.

# Main Example
a = [1, 2, 3]
b = a            # b points to the same object as a 
c = [1, 2, 3]    # new list with the same VALUE but a different ID (new object)

# Identity (same object or not)
print("IDENTITY CHECK (is):")

print("id(a):", id(a))
print("id(b) (same ID as a):", id(b)) # same ID as a
print("id(c) (ifferent ID):", id(c)) # different ID

print("a is b →", a is b)  # True  → same identity (both point to same object)
print("a is c →", a is c)  # False → same value but different identity

"""
💡 NOTE: Equality checks *memory addresses*, not values.
"""

# Equality (same value or not)
print("\nEQUALITY CHECK (==):")
print("a == b →", a == b)  # True → same content (same identity)
print("a == c →", a == c)  # True → same content (different identity)

"""
💡 NOTE: Equality checks *values*, not memory addresses.
"""

# ---------------------------
# Mutability demonstration
# ---------------------------
print("\nMUTABILITY:")
b.append(4)  # modifies the shared list (because a and b share identity)

print("a:", a)  # [1, 2, 3, 4]  → a changed too! Because it references the same object as b
print("b:", b)  # [1, 2, 3, 4]
print("c:", c)  # [1, 2, 3]     → unchanged, separate object

# ======================================================
# 🌀 EXTRA knowledge: COPIES — shallow vs deep
# ======================================================
print("\nCOPIES — shallow vs deep:")
import copy

# Shallow copy: duplicates the outer container, reuses references of inner items
outer = [[1], [2]]
shallow = list(outer)       # equivalent to outer.copy() or outer[:]
outer[0].append(99)

print(outer)    # [[1, 99], [2]]  # inner lists are modified
print(shallow)  # [[1, 99], [2]]  # inner lists are shared references because of shallow copy

# Deep copy: recursively duplicates inner structures
outer2 = [[1], [2]]
deep = copy.deepcopy(outer2)
outer2[0].append(77)

print(outer2)   # [[1, 77], [2]] # inner lists are modified
print(deep)     # [[1], [2]]     # inner lists are independent copies because of deep copy