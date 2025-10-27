# ---------------------------
# 🌀 VARIABLE SCOPE - PART 01
# ---------------------------

# 1️⃣ Global variable
x = 10

def my_function():
    # Local variable
    y = 5
    print(f"Inside function -> x: {x}")  # Access global
    print(f"Inside function -> y: {y}")  # Local only

my_function()

# Accessing global variable outside function
print(f"Outside function -> x: {x}")

# Uncommenting the next line would raise an error
# print(y)  # ❌ NameError: 'y' is not defined (y is local)

# 2️⃣ LOCALS() - Show local scope mapping

def show_scope():
    a = 10
    b = [1, 2, 3]
    print("Local scope mapping:")
    print(locals())  # Shows the current local variable bindings

show_scope()

# 3️⃣ LEGB RULE EXAMPLE (Local → Enclosing → Global → Built-in)

x = "global"

def outer():
    x = "enclosing" #if you comment this line, it will print "global"
    def inner():
        x = "local" #if you comment this line, it will print "enclosing"
        print(f"Value of x (LEGB order): {x}")
    inner()

outer()
# Output: "local" → Python starts from Local, then Enclosing, Global, Built-in


# ---------------------------
# 🌀EXTRA knowledge: BUILT-IN FUNCTIONS
# ---------------------------

# Using built-in functions
numbers = [10, 20, 30]
print("Built-in len():", len(numbers))
print("Built-in max():", max(numbers))
print("Built-in sum():", sum(numbers))
print("Built-in type():", type(numbers))

# Show some built-in functions names
import builtins
print("\nShow some built-in names:")
print(dir(builtins)[:15])  # Show the first 15 built-in names