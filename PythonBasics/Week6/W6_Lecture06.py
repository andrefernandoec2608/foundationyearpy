# ---------------------------
# 🌀 RAISE & CUSTOM EXCEPTIONS & EXCEPTION HIERARCHY
# ---------------------------
# Python throws an exception with raise
# We can also define our own exception classes (by inheriting from Exception or its subclasses)
# This is useful for validation, domain-specific errors, and app-wide error handling.

# 1️⃣ RAISE BUILT-IN EXCEPTIONS
# The 'raise' keyword is used to manually trigger an exception

# Example function that raises a ValueError if age is negative
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age must be non-negative")
    print("✅ Age set:", age)

"""
💡 NOTE:
TypeError and ValueError are built-in exceptions:
- TypeError → wrong data type (e.g., "10" + 5)
- ValueError → right type but invalid value (e.g., int("abc"))
"""

# Example usage
try:
    set_age(-5)
except ValueError as e:
    print("Caught:", e)  # Caught: Age must be non-negative

# 2️⃣ CUSTOM A 'ValueError' EXCEPTION
#  We can create our own exception classes by inheriting from any built-in exceptions or its subclasses
# This allows us to add custom attributes or methods for more specific error handling.

# Here, we create a custom AgeError that extends ValueError
class AgeError(ValueError):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
    def __str__(self):
        # Customize printed message
        return f"{super().__str__()} (code={self.code})"

# Example function that raises our custom exception
def validate_age(age):
    if age > 50:
        raise AgeError("Age must be lower than 50", 100)
    if age < 0:
        raise AgeError("Age must be positive", 200)
    print("✅ Valid age:", age)

# Example usage
try:
    validate_age(55)
except AgeError as e:
    print("Caught custom:", e)          # Caught custom: Age must be integer (code=100)
    print("Error code:", e.code)        # Error code: 100

# 3️⃣ EXCEPTION HIERARCHY DEMONSTRATION
# We can create a hierarchy of custom exceptions for better error categorization

# # Here, we create a base exception and two derived exceptions
class AppError(Exception):         # base class for app-related errors
    pass
class ValidationError(AppError):   # group validation issues
    pass
class DatabaseError(AppError):     # group DB-related issues
    pass

# Example function that raises different exceptions
def save_user(name: str, age: int):
    raise DatabaseError("DB connection timeout") # Imagine DB failure.

# Example usage
"""
💡 NOTE: Catching specific exceptions first, then more general ones
"""
try:
    save_user("ELTE", 7)
except ValidationError as e:
    print("Validation error:", e)
except DatabaseError as e:
    #  This block will be executed because save_user raises DatabaseError
    print("Database error:", e) # Output: Database error: DB connection timeout
except AppError as e:
    print("Generic app error:", e) # would catch any AppError not matched above

"""
🌀 EXTRA knowledge: Common Categories of Built-in Exceptions in Python

### 1 Type & Value Errors
   - TypeError → wrong data type used in an operation.
     Example: "10" + 5
   - ValueError → correct type but invalid value.
     Example: int("abc")

### 2 Numeric Errors
   - ZeroDivisionError → division or modulo by zero.
   - OverflowError → numeric result too large to represent.

### 3 Name & Attribute Errors
   - NameError → variable or name not defined.
   - AttributeError → object has no such attribute or method.

### 4 Index & Key Errors
   - IndexError → index out of range in a list or tuple.
   - KeyError → key not found in a dictionary.

### 5 I/O & File Errors
   - FileNotFoundError → file or path does not exist.
   - IOError (OSError) → general input/output operation failure.
"""