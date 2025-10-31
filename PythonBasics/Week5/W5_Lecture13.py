# ---------------------------
# 🌀 OBJECT LIFECYCLE (__new__, __init__, __del__)
# -----------------------------------
# In Python, every object goes through a lifecycle:
# Full object lifecycle is creation → initialization → use → destruction.

# ⚠️ ALERT: OBJECT LIFECYCLE STAGES
# 1) CREATION: allocate/return a new instance (memory level).
# 2) INITIALIZATION: configure attributes/state.
# 3) USE: Methods run; object participates in the program.
# 4) DESTRUCTION: Garbage Collector finalizes objects if no references remain and executes __del__ if defined.
# 🗑️ Garbage Collector (GC) automatically frees memory by reclaiming objects that are no longer referenced.

# -----------------------------------
# 1️⃣ Creation (__new__), Initialization (__init__), Destruction (__del__)
# -----------------------------------
class Pizza:
    def __new__(cls, *args, **kwargs):
        # Creation stage: memory allocation, returns the new instance
        print("🔧 __new__() → Allocating memory for a new Pizza object.")
        instance = super().__new__(cls)  # call object.__new__(cls)
        return instance

    def __init__(self, name):
        # Initialization stage: set up attributes
        print(f"🍕 __init__() → Initializing Pizza with name: {name}")
        self.name = name

    def __del__(self):
        # __del__ timing is NOT guaranteed.
        # It runs when the GC finalizes the object.
        print(f"💀 __del__() → Pizza '{self.name}' finalized.")

# -----------------------------------
# 2️⃣ Object creation and reference behavior
# -----------------------------------
p = Pizza("Margherita")
del p # 🌀 del removes a reference;
# 💡 NOTE: __del__ executes only when no references remain and is decided by the GC

# Multiple references example
p2 = Pizza("Pepperoni")
p3 = p2
del p2 # 💡 NOTE: Pizza still exists because 'p3' still points to it.
del p3 # Now no references remain, so the GC can finalize the object and call __del__()

"""
💡 NOTE: When would you override __new__?
For advanced metaprogramming, when shaping the object BEFORE __init__.
"""

"""
⚠️ ALERT: Why relying on __del__ can be risky:
• You can't control exactly WHEN it runs (GC decides; might be delayed).
• Some code inside __del__ might be ignored.
"""