# ---------------------------
# 🌀 EXCEPTION HANDLING    
# ---------------------------
# Errors happen! Exception handling lets us detect and manage them gracefully,
# preventing crashes and allowing safer, more predictable programs.

# 1️⃣ BASIC try / except
print("=== Basic try / except ===")
try:
    x = 10 / 0
    print("Result:", x) # This line won't execute because of the error above
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")  # Output: ❌ Cannot divide by zero!

# 2️⃣ CAPTURING ERROR DETAILS
print("=== Capturing error details (as e) ===")
try:
    y = int("abc")
except ValueError as e:
    print("⚠️ ValueError:", e)  # Output: ⚠️ ValueError: invalid literal for int() with base 10: 'abc'

# 3️⃣ MULTIPLE EXCEPTIONS
print("=== Multiple exception handling ===")
try:
    a = int(input("Enter numerator: "))     # Example input: 10
    b = int(input("Enter denominator: "))   # Example input: 0
    print("Result:", a / b)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("⚠️ Only numeric input is allowed.")

"""
💡 NOTE:
The 'except' block that matches the raised error is executed first.
If none match, the error propagates (as if it weren't inside the 'try' block).
"""

# 4️⃣ ELSE and FINALLY
print("=== try / except / else / finally ===")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("❌ Division error.")
else:
    print("✅ No exception, result =", result)  # Runs if no error
finally:
    print("🧹 Finally block executed (cleanup code)")  # Always runs

"""
💡 NOTE:
Else: Executes only if no exception occurred.
Finally: always executed, regardless of whether an error occurred (ideal for clean-up or closure).
"""

# 5️⃣ GENERIC EXCEPTION HANDLER (use with care)
# Catch-all handler: useful for debugging, but hides specific error types — avoid in production
print("=== Generic handler (not recommended for production) ===")
try:
    lst = [1, 2, 3]
    print(lst[5])       # There is an IndexError
except Exception as e:  # Catch-all for any exception
    print("⚠️ Some error occurred:", type(e).__name__, "-", e)