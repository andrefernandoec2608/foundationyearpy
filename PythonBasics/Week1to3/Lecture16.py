# ---------------------------
# 🌀 LIST BASICS & OPERATIONS - Part 01
# ---------------------------
#   Understanding lists, creating, modifying, aliasing vs cloning,

# 1️⃣ Creating and modifying lists
#  Lists are ordered, mutable collections of items (can contain duplicates and mixed types)
fruits = ["apple", "banana", "cherry"]
fruits.append("banana")             # add one element at the end
print(fruits)                       # ['apple', 'banana', 'cherry', 'banana']

# Modify an element by index
del fruits[0]                       # delete element by index
print("After deleting index 0:", fruits) # ['banana', 'cherry', 'banana']

# extend the list with multiple elements
fruits.extend(["grape", "melon"])   # add multiple elements at the end
print("After extend:", fruits)      # ['banana', 'cherry', 'banana', 'grape', 'melon']

# 2️⃣ ALIASING vs CLONING
# Aliasing → both names refer to the same object
numbers = [10, 20, 30]
alias_numbers = numbers                             # both point to the same list
del alias_numbers[0]                                # modifies both
print("Original list after alias change:", numbers) # [20, 30]

# Cloning → create a new copy (shallow copy)
cloned_numbers = numbers[:]                         # independent copy
del cloned_numbers[0]                               # modifies only the clone
print("Original list:", numbers)                    # [20, 30]
print("Cloned list:", cloned_numbers)               # [30]

# 3️⃣ MIXED TYPE LISTS
# Lists can contain elements of different types
mixed = [1, 2.5, "hello", (3, 4)]
print("Mixed type list:", mixed)

# Membership test
if "hello" in mixed:
    print("'hello' is inside mixed list")

# 4️⃣ LIST LENGTH AND INDEXING
# You can get the length of a list and access elements by index
empty_list = []
nums = [1, 2, 3, 4]
complex_list = ["I", "am", 30, [1, 2]]

print("Length of empty list:", len(empty_list))
print("Length of nums:", len(nums))
print("Length of complex_list:", len(complex_list))

print("First element of nums:", nums[0])
print("Last element of complex_list:", complex_list[-1])
print("Reversed complex_list:", complex_list[::-1])