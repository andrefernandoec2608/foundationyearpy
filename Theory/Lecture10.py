# ---------------------------
# VARIABLE SCOPE (GLOBAL & NONLOCAL)
# ---------------------------

# ---------- Global variable ----------
x = 10  # global variable

def show_scope():
    y = 5  # local variable
    print("Inside function -> local y:", y)
    print("Inside function -> global x (read):", x)

show_scope()
print("Outside function -> global x:", x)
# print(y)  # ❌ would raise NameError (y is local)


# ---------- Modifying global variable ----------
# By default, you cannot modify a global variable directly inside a function.
# You need to use the 'global' keyword.

count = 0  # global variable

def increment():
    global count
    count += 1
    print("Inside increment() -> count:", count)

for _ in range(3):
    increment()

print("Outside function -> count:", count)


# ---------- Functions without 'global' ----------
# Without the keyword, Python creates a NEW local variable (does not touch the global one).

x = 100

def modify_local():
    x = 50  # local variable with same name as global
    print("Inside modify_local() -> x:", x)

modify_local()
print("Outside after modify_local() -> global x:", x)  # unchanged


# ---------- Using NONLOCAL ----------
# 'nonlocal' allows inner functions to modify variables
# from their enclosing (outer) function scope.

def outer():
    message = "Hello (outer)"

    def inner():
        nonlocal message
        message = "Modified by inner"
        print("Inside inner() -> message:", message)

    inner()
    print("Inside outer() after inner() -> message:", message)

outer()