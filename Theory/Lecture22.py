# ---------------------------
# 2️⃣ LIST ALIASING & 'del list[:]' SUMMARY
# ---------------------------

# Step 1: All variables reference the same list object
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

# Visual model:
# ┌───────────────┐
# │ ["A","B","C"] │
# └───────────────┘
#   ↑     ↑     ↑
# list_1 list_2 list_3

# Step 2: Delete the first element (index 0)
del list_2[0]      # removes "A"
print("After del list_1[0]:", list_3) # it affects all references
# Output: ['B', 'C']

# Step 3: Delete all elements using slice [:]
del list_3[:]      # empties the SAME list object
print("After del list_3[:]:", list_1)
# Output: []

# Visual model now:
# ┌───────────────┐
# │      []       │
# └───────────────┘
#   ↑     ↑     ↑
# list_1 list_2 list_3

# Step 4: Delete the variable reference
x = [1, 2, 3]
y = x
del y[:]     # empties the list (keeps both variables)
print(x)     # []
print(y)     # []

x = [1, 2, 3]
y = x
del y        # deletes the variable name only
print(x)     # [1, 2, 3]
# print(y)   # ❌ NameError: y is not defined