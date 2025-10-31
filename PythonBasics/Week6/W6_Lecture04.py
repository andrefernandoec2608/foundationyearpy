# ---------------------------
# 🌀 CONTEXT MANAGER - Implementing __enter__ and __exit__ methods
#
# The 'with' statement is not just for files — it works with any object
# implementing two special methods:
#   __enter__(self) → runs when entering the with-block
#   __exit__(self, exc_type, exc_val, exc_tb) → runs when leaving (used for cleanup)
# This is called the Context Manager Protocol.
# It allows defining your own logic to manage resources safely and automatically.

# 💡 NOTE: If any ERROR occurs inside the 'with' block, Python passes three arguments to __exit__ method:
#   exc_type → type of the exception (ZeroDivisionError, ValueError, etc.)
#   exc_val  → message or value of the exception
#   exc_tb   → traceback (location and call stack info)
# ---------------------------

# 1️⃣ Defining a custom context manager class
class MyResource:
    def __enter__(self):
        print("✅ Resource acquired")   # runs at the start of 'WITH' statement block
        self.value = 10                 # simulate a resource value or setup
        return self                     # returned object is assigned to the variable after 'as' in the 'WITH' statement
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🧹 Resource released (cleanup)")  # always runs when leaving the 'WITH' statement block
        
        if exc_type: # if an exception occurred inside the 'WITH' statement block
            print(f"⚠️ Exception handled:")
            print(f"   exc_type: {exc_type.__name__}")
            print(f"   exc_val : {exc_val}")
            print(f"   exc_tb  : {exc_tb.tb_lineno} (line number of the error)")
        
        # ⚙️ About return value:
        # Returning True  → suppresses the exception (program continues normally)
        # Returning False → lets the exception propagate (normal behavior)
        # Here we return True just for demo purposes, so the script won't crash.
        return True

# 2️⃣ Using the custom context manager with 'WITH' statement

# Before the 'WITH' statement block
print(">>> Entering with-block")

# This is the 'WITH' statement block using our custom context manager class
# By the way, here we simulate a division by zero error.
with MyResource() as r:
    print("🔧 Using resource with value:", r.value)
    result = r.value * 2
    print("✅ Computation result:", result)
    
    print("⏳ Simulating an error now...")
    x = 10 / 0   # triggers ZeroDivisionError but handled by __exit__ method
    print("This line won't be reached") # because of the error

# After the 'WITH' statement block
print(">>> Exited with-block safely (resource auto-cleaned)")