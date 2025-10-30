# ---------------------------
# 🌀 MAP() AND LIST()
# ---------------------------

# 1️⃣ map(function, iterable)
# map() applies a function to every element in an iterable (like a list or tuple)
# and returns a map object (which is an iterator).

def double(x):
    return x * 2

numbers = [1, 2, 3, 4]

# map() applies 'double' to each element in 'numbers'
doubled = map(double, numbers)

print("Result of map():", doubled)   # This is a map object (iterator)
print("Doubled numbers (as list):", list(doubled))  # Convert to list to see values


# 2️⃣ list(iterable)
# list() converts any iterable (map, range, tuple, etc.) into a Python list.

nums = range(5)
print("List from range:", list(nums))

# 4️⃣ Using map() with a built-in function
words = ["hello", "python", "world"]
uppercased = map(str.upper, words)
print("Uppercased words:", list(uppercased))


# 5️⃣ You can combine map() and list() for quick transformations
# Example: convert numbers to strings
numbers = [1, 2, 3]
as_strings = list(map(str, numbers))
print("Numbers as strings:", as_strings)