# ---------------------------
# 🌀 ITERABLES & ITERATORS vs FILTERING vs SORTING vs RANGES
# ---------------------------

# 1️⃣ ITERABLES & ITERATORS
# An iterable is any object capable of returning its members one at a time.

# An iterator is an object that represents a stream of data;
# You can obtain an iterator from an iterable by calling iter().
# Iterator returns the next item when you call next() on it.

# Examples of iterables:
# - Built-in collections: list, tuple, dict, set
# - Strings
# - range objects
# - File objects
# Custom classes that implement the __iter__() method.

### MANUAL ITERATION USING iter() and next()
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Throw the exception: StopIteration

### ITERATION PATTERNS USING for LOOPS (pythonic iteration)
# The for loop construct in Python is the preferred way to iterate over elements.
# It automatically handles the iterator protocol for you.
# It abstracts away the iterator protocol
# It works with any iterable type and avoids off-by-one/index errors.

# BASIC FOR LOOP USAGE
# Simple examples of iterating through different iterable types.

# Iterate through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())  # APPLE / BANANA / CHERRY

# Iterate through a string (character by character)
for ch in "AI":
    print(ch)  # A / I

# Iterate through a tuple
coords = (10, 20, 30)
for val in coords:
    print(val)  # 10 / 20 / 30

# Iterate through a dict (keys by default)
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])  # name Alice / age 30

# Iterate through key-value pairs directly
for k, v in person.items():
    print(f"{k} -> {v}")  # name -> Alice / age -> 30


# 2️⃣ TRANSFORMATION & FILTERING PATTERNS
# Common patterns for transforming or filtering data from iterables.

### List comprehensions (idiomatic & very common)
# - Provide a concise way to create lists.
# - Can include conditions for filtering.
# - More readable for simple transformations/filters.
# Example usages:
numbers = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in numbers]                 # transform
evens   = [n for n in numbers if n % 2 == 0]      # filter
print(squares)  # [1, 4, 9, 16, 25, 36]
print(evens)    # [2, 4, 6]

### Functional programming style (less common than comprehensions)

# - Both return iterators, so we often wrap them in list() to get a list.
# - They can be more efficient for large datasets since they are lazy.
# - map() and filter() can improve readability when using named functions.
# 
# - map(func, iterable) applies func to each element.
# - filter(pred, iterable) keeps elements where pred(element) is True.
# Example usages:

# Using lambda functions for inline transformations/filters:
squares_map = list(map(lambda n: n**2, numbers))           # ~ [n**2 for n in numbers]
evens_filter = list(filter(lambda n: n % 2 == 0, numbers)) # ~ [n for n in numbers if n % 2 == 0]
print(squares_map)   # [1, 4, 9, 16, 25, 36]
print(evens_filter)  # [2, 4, 6]

# Using existing named functions can make map/filter more readable:
def is_even(x: int) -> bool:
    return x % 2 == 0
def square(x: int) -> int:
    return x * x

print(list(filter(is_even, numbers)))  # [2, 4, 6]
print(list(map(square, numbers)))      # [1, 4, 9, 16, 25, 36]

"""
💡 NOTE:
For simple inline transformations/filters, list comprehensions are preferred for readability.
"""

# 3️⃣ SORTING ITERABLES
# Two main ways to sort in Python:
names = ["Zoe", "alex", "Bob", "claire"]

# - sorted(iterable, ...) → returns a NEW sorted list (non-destructive).
sorted_names = sorted(names)  # default (case-sensitive)
print(sorted_names)  # ['Bob', 'Zoe', 'alex', 'claire']  (uppercase letters come first in ASCII)
sorted_names_ci = sorted(names, key=str.lower)  # case-insensitive
print(sorted_names_ci)  # ['alex', 'Bob', 'claire', 'Zoe']

# - list.sort(...)       → sorts IN PLACE (mutates the original list).
names.sort(key=str.lower, reverse=True)  # in-place, case-insensitive, descending
print(names)  # ['Zoe', 'claire', 'Bob', 'alex']

# 4️⃣ RANGE — lightweight numeric iterable
# range(start, stop[, step]) produces numbers lazily (does not pre-build a list).
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(3)))         # [0, 1, 2]

"""
💡 NOTE: FILE OBJECTS ARE ITERABLE (REFERENCE ONLY)
# A file opened in "r" mode yields lines (each iteration returns a string, often ending with '\n').
# Typical pattern (shown here as a comment; we will practice in the File Handling module):

with open("sample.txt", "r") as f:
    # Iterate line by line (memory-efficient for large files)
    lines_upper = []
    for line in f:
        lines_upper.append(line.rstrip("\n").upper())  # strip newline, transform
    print(lines_upper)  # Example: ['APPLE', 'BANANA', 'CHERRY']
"""

# 🌀 EXTRA knowledge: ZIP & ENUMERATE (handy iterable helpers)

# enumerate() and zip() are built-in functions that simplify common iteration patterns.
# They return iterables that can be looped over directly.
# Useful for getting indices or pairing elements from multiple iterables.

# Example usages:
# enumerate(iterable, start=1) → (index, value) pairs
for i, fruit in enumerate(["a", "b", "c"], start=1):
    print(f"{i}: {fruit}")  # 1: a / 2: b / 3: c

# zip(*iterables) → pairs items element-wise until the shortest iterable is exhausted
names2  = ["Alice", "Bob", "Charlie"]
scores2 = [95, 82, 100]
pairs = list(zip(names2, scores2))
print(pairs)  # [('Alice', 95), ('Bob', 82), ('Charlie', 100)]