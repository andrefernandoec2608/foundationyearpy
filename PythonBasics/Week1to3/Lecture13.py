# ---------------------------
# 🌀 FUNCTION --> RETURN
# ---------------------------
# Functions in Python can return any type of object.
# A function can return numbers, strings, lists, dicts, or even other functions.

# Return a number
def get_number():
    return 42

# Return a string
def get_greeting():
    return "Hello, Python!"

# Return a list
def get_list():
    return [1, 2, 3, 4, 5]

# Return a dictionary
def get_person():
    return {"name": "Alice", "age": 25}

# --- Calling the functions ---
print("Number:", get_number())
print("Greeting:", get_greeting())
print("List:", get_list())
print("Dictionary:", get_person())

# Return another function
def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    return inner_function  # returning the function itself

# Returning another function
func = outer_function()
func()  # call the returned inner function

# Returning multiple values (tuple packing)
def get_data():
    return 10, "Alice", [1, 2, 3]

a, b, c = get_data()
print("Multiple return values:", a, b, c)