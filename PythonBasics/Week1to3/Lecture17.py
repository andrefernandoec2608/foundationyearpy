# ---------------------------
# 🌀 LIST BASICS & OPERATIONS - Part 02
# ---------------------------
# Understanding lists and basic list operations in Python

# ---------------------------
# 🌀 SLICING AND REVERSING
# ---------------------------
# Slicing: list[start:stop:step] --> Extracts a portion of the list
# start: starting index (inclusive)
# stop: ending index (exclusive)
# step: step size (default is 1)
# Negative indices can be used to count from the end

# Example:
letters = ["a", "b", "c", "d", "e", "f"]
print("Slice [1:4]:", letters[1:4])      # ['b', 'c', 'd']
print("Slice [::2]:", letters[::2])      # every 2nd element
letters.reverse()                        # reverse in place
print("Reversed list:", letters)


# ---------------------------
# 🌀 REMOVING ELEMENTS
# ---------------------------
# Various ways to remove elements from a list
# Using del, pop(), and remove()
data = [5, 2, 3, 4, 7, "I", "am", 30, [1, 2]]
del data[5]                              # delete element by index
print("After del:", data)

last_item = data.pop()                   # removes and returns last element
print("Popped element:", last_item)
print("After pop:", data)

# ---------------------------
# 🌀 SORTING LISTS
# ---------------------------
# Sorting lists using sorted() and .sort()

# sorted() returns a new sorted list, .sort() sorts the list in place
# Example:
unsorted_list = [4, 1, 3, 2]
print("Sorted copy:", sorted(unsorted_list))  # returns a new list
print("Original list (unchanged):", unsorted_list)

# .sort() method sorts the list in place
# It means it directly modifies the original list — it doesn't create a new one.
unsorted_list.sort()                          # sorts in place
print("After .sort():", unsorted_list)