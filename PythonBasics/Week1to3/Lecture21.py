# ---------------------------
# 🌀 FUNCTION RETURN
# ---------------------------
# ✅ Understanding the return statement in Python functions

# When Python executes a return, it immediately exits the function, no matter what comes after it.
def example():
    print("Before return")
    return
    print("After return")   # This line is NEVER executed
example()

# return without explicit value returns None
def func_a():
    return
result = func_a()
print(result)

def with_return():
    return "Hello"

# Quick example comparison
def without_return():
    print("Hello")

print(with_return())   # Output: Hello
print(without_return()) # Output: Hello + None