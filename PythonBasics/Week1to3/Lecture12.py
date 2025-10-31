# ---------------------------
# 🌀 FUNCTION --> ARGUMENT ORDER
# ---------------------------

# 1️⃣ Correct order when DEFINING a function:
# positional → default → *args → **kwargs

def example_func(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

# 2️⃣ Correct order when CALLING a function:
# positional → keyword

print("\n--- Correct function call ---")
example_func(1, 2, 3, 4, x=5, y=6)
# a = 1  → positional
# b = 2  → positional
# args = (3, 4)
# kwargs = {'x': 5, 'y': 6}

# ✅ You can also call with keyword arguments explicitly
print("\n--- Call with keywords ---")
example_func(a=1, b=2, x=100, y=200)

# 3️⃣ Incorrect 🚫 definition (will cause SyntaxError)
# def wrong_func(*args, a, **kwargs):   # ❌ cannot define like this
#     pass

# 4️⃣ Incorrect 🚫 call (positional after keyword)
print("\n--- Incorrect call example ---")
# example_func(a=1, 2, 3)  # ❌ positional argument after keyword
# This line would raise: SyntaxError: positional argument follows keyword argument

# 5️⃣ Using *args and **kwargs to forward arguments to another function
def wrapper(*args, **kwargs):
    print("Wrapper received:", args, kwargs)
    example_func(*args, **kwargs)

print("\n--- Using wrapper with *args and **kwargs ---")
wrapper(10, 20, 30, x=1000, y=2000) 