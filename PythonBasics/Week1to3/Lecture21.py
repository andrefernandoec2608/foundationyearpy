# ---------------------------
# 🌀 FUNCTION RETURN
# ---------------------------
# Understanding the return statement in Python functions

# When Python executes a return, it immediately exits the function, no matter what comes after it.
def example():
    print("Before return")
    return
    print("After return")   # This line is NEVER executed
example()

# return without explicit value returns None
def func_a():
    return # Implicitly returns None
result = func_a()
print(result)

# return with explicit value returns that value
def with_return():
    return "Hello" # Explicitly returns "Hello"
result = with_return()
print(result)

# Quick example comparison
# Function with return value vs function without return value
def without_return():
    print("Hello")

print(with_return())   # Output: Hello
print(without_return()) # Output: Hello + None
# if you don't get it, run the code to see the difference!