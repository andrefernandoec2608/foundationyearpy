# ---------------------------
# 🌀 FUNCTION CAN RECEIVE ANOTHER FUNCTION
# ---------------------------

# Simple functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# Function that accepts another function as argument
def greet(func):
    # 'func' is a function passed as an argument
    message = func("Hello, Friend!")
    print(message)

# Passing different functions as arguments
greet(shout)
greet(whisper)


# Built-in functions as arguments
def apply_function(func, value):
    return func(value)

print("Absolute value:", apply_function(abs, -10))
print("Length:", apply_function(len, "Python"))


# Function as variable
def square(x):
    return x * x

operation = square  # assign function to a variable
print("Square using variable:", operation(5))


# Using map() to apply a function to all elements
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled = map(double, numbers)
print("Doubled numbers:", list(doubled))