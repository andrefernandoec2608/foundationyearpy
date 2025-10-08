# ---------------------------
# 🌀 LIST BASICS & OPERATIONS
# ---------------------------

# Creating and modifying lists
fruits = ["apple", "banana", "cherry"]
fruits.append("peach")             # add one element at the end
print("After append:", fruits)

del fruits[0]                      # delete element by index
print("After deleting index 0:", fruits)

fruits.extend(["grape", "melon"])  # add multiple elements
print("After extend:", fruits)


# ---------------------------
# ALIASING vs CLONING
# ---------------------------

# Aliasing → both names refer to the same object
numbers = [10, 20, 30]
alias_numbers = numbers            # both point to the same list
del alias_numbers[0]               # modifies both
print("Original list after alias change:", numbers)

# Cloning → create a new copy (shallow copy)
cloned_numbers = numbers[:]        # independent copy
del cloned_numbers[0]
print("Original list:", numbers)
print("Cloned list:", cloned_numbers)


# ---------------------------
# MIXED TYPE LISTS
# ---------------------------

mixed = [1, 2.5, "hello", (3, 4)]
print("Mixed type list:", mixed)

# Membership test
if "hello" in mixed:
    print("'hello' is inside mixed list")


# ---------------------------
# LIST LENGTH AND INDEXING
# ---------------------------

empty_list = []
nums = [1, 2, 3, 4]
complex_list = ["I", "am", 30, [1, 2]]

print("Length of empty list:", len(empty_list))
print("Length of nums:", len(nums))
print("Length of complex_list:", len(complex_list))

print("First element of nums:", nums[0])
print("Last element of complex_list:", complex_list[-1])
print("Reversed complex_list:", complex_list[::-1])